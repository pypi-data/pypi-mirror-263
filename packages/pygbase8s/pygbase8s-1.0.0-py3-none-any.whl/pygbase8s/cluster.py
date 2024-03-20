# coding: utf-8
# @Time    : 2024/3/5 10:01
# @Author  : wangwei
from abc import ABCMeta, abstractmethod
from pygbase8s.server import Server


class Cluster(metaclass=ABCMeta):
    """
    GBase 8s集群抽象类
    """

    def __init__(self, primary_node: Server, bak_node: Server):
        """
        :param primary_node: SERVER, 主节点
        :param bak_node: SERVER, 备节点
        """
        self._primary_node = primary_node
        self._bak_node = bak_node

    @abstractmethod
    def initialize(self):
        """
        集群初始化
        :return:
        """
        pass

    @property
    def primary_node(self):
        """
        返回集群的主节点
        :return: SERVER
        """
        return self._primary_node


    @property
    def bak_node(self):
        """
        返回集群的备节点
        :return: SERVER
        """
        return self._bak_node

    def release(self):
        """
        释放集群
        :return:
        """
        self.primary_node.release()
        self.bak_node.release()

    def set_trust(self):
        """
        配置互信
        :return:
        """
        self.primary_node.ids.machine.trust(self.bak_node.ids.machine)


class SDSCluster(Cluster):
    """
    SDS集群类
    """
    type = 'SDS'

    def initialize(self):
        """
        初始化SDS集群
        :return:
        """
        if self.primary_node.ip != self.bak_node.ip:
            self.set_trust()
        self.bak_node.onconfig.set_variable('SDS_ENABLE', '1')
        self.bak_node.onconfig.set_variable('SDS_PAGING', '{0}/sdstmp1,{0}/sdstmp2'.format(self.bak_node.path))
        self.bak_node.onconfig.set_variable('SDS_TEMPDBS',
                                            f'sdstmpdbs1, {self.bak_node.path}/sdstmpdbs1,2,0,16000')
        code, out = self.bak_node.run_cmd(f"mkdir -p {self.bak_node.path};chmod 755 {self.bak_node.path}")
        if code != 0:
            raise Exception(f"备节点创建存储目录失败，错误码{code}, 错误信息{out}")
        code, out = self.bak_node.run_cmd(f'cd {self.bak_node.path}; touch sdstmp1 sdstmp2;chown gbasedbt:gbasedbt sdstmp1 sdstmp2;'
                              f' chmod 660 sdstmp1 sdstmp2')
        if code != 0:
            raise Exception(f"备节点创建sdstmp失败，错误码{code}, 错误信息{out}")
        code, out = self.bak_node.run_cmd(
            f'cd {self.bak_node.path}; touch sdstmpdbs1;chown gbasedbt:gbasedbt sdstmpdbs1; chmod 660 sdstmpdbs1')
        if code != 0:
            raise Exception(f"备节点创建sdstmpdbs失败，错误码{code}, 错误信息{out}")

        self.primary_node.sqlhosts.add_server(self.bak_node.name, self.bak_node.ip, self.bak_node.port)
        self.bak_node.sqlhosts.add_server(self.primary_node.name, self.primary_node.ip, self.primary_node.port)
        self.primary_node.initialize()
        code, out = self.primary_node.run_cmd(f'onmode -d set SDS primary {self.primary_node.name}')
        if code != 0:
            raise Exception(f"主节点set SDS primary 失败，错误码{code}, 错误信息{out}")
        if self.primary_node.ip == self.bak_node.ip:
            self.bak_node.path = self.primary_node.path
        self.bak_node.startup()


class HDRCluster(Cluster):
    """
    HDR集群类
    """
    type = 'HDR'

    def initialize(self):
        """
        初始化HDR集群
        :return:
        """
        if self.primary_node.ip != self.bak_node.ip:
            self.set_trust()
        for node in [self.primary_node, self.bak_node]:
            node.onconfig.set_variable('DRAUTO', '3')
            node.onconfig.set_variable('DRINTERVAL', '30')
            node.onconfig.set_variable('DRTIMEOUT', '30')
            node.onconfig.set_variable('HA_FOC_ORDER', 'HDR')
            node.onconfig.set_variable('UPDATABLE_SECONDARY', '0')
            node.onconfig.set_variable('DRLOSTFOUND', '$GBASEDBTDIR/etc/dr.lostfound')
        self.primary_node.sqlhosts.add_server(self.bak_node.name, self.bak_node.ip, self.bak_node.port)
        self.bak_node.sqlhosts.add_server(self.primary_node.name, self.primary_node.ip, self.primary_node.port)
        self.primary_node.initialize()
        code, out = self.primary_node.run_cmd(f'onmode -d primary {self.bak_node.name}')
        if code != 0:
            raise Exception(f"主节点执行onmode -d primary失败，错误码{code}, 错误信息{out}")
        # 主做0及备份
        code ,out = self.primary_node.run_cmd(f'ontape -s -L 0 -t STDIO > /tmp/tape_L0', cwd=self.primary_node.path)
        if code != 0:
            raise Exception(f"主节点执行0级备份失败，错误码{code}, 错误信息{out}")
        if self.primary_node.ip != self.bak_node.ip:
            self.primary_node.ids.machine.download('/tmp/tape_L0', 'tape_L0')
            self.bak_node.ids.machine.upload('tape_L0', '/tmp/tape_L0')
        # 备做备份恢复
        self.bak_node._add_chunk_file('rootdbs')
        code, out = self.bak_node.run_cmd('cat /tmp/tape_L0|ontape -p -t STDIO', cwd=self.bak_node.path)
        if code != 0:
            raise Exception(f"备节点执行备份恢复失败，错误码{code}, 错误信息{out}")
        code, out = self.bak_node.run_cmd(f'onmode -d secondary {self.primary_node.name}')
        if code != 0:
            raise Exception(f"备节点执行onmode -d secondary失败，错误码{code}, 错误信息{out}")


class RSSCluster(Cluster):
    """
    RSS集群类
    """
    type='RSS'

    def initialize(self):
        """
        初始化RSS集群
        :return:
        """
        if self.primary_node.ip != self.bak_node.ip:
            self.set_trust()
        self.primary_node.onconfig.set_variable('LOG_INDEX_BUILDS', '1')
        self.primary_node.sqlhosts.add_server(self.bak_node.name, self.bak_node.ip, self.bak_node.port)
        self.bak_node.sqlhosts.add_server(self.primary_node.name, self.primary_node.ip, self.primary_node.port)
        self.primary_node.initialize()
        code, out = self.primary_node.run_cmd(f'onmode -d add RSS {self.bak_node.name}')
        if code != 0:
            raise Exception(f"主节点执行onmode -d add RSS失败，错误码{code}, 错误信息{out}")
        # 主做0及备份
        code, out = self.primary_node.run_cmd(f'ontape -s -L 0 -t STDIO > /tmp/tape_L0', cwd=self.primary_node.path)
        if code != 0:
            raise Exception(f"主节点执行0级备份失败，错误码{code}, 错误信息{out}")
        if self.primary_node.ip != self.bak_node.ip:
            self.primary_node.ids.machine.download('/tmp/tape_L0', 'tape_L0')
            self.bak_node.ids.machine.upload('tape_L0', '/tmp/tape_L0')
        # 备做备份恢复
        self.bak_node._add_chunk_file('rootdbs')
        code, out = self.bak_node.run_cmd('cat /tmp/tape_L0|ontape -p -t STDIO', cwd=self.bak_node.path)
        if code != 0:
            raise Exception(f"备节点执行备份恢复失败，错误码{code}, 错误信息{out}")
        code, out = self.bak_node.run_cmd(f'onmode -d RSS {self.primary_node.name}')
        if code != 0:
            raise Exception(f"备节点执行onmode -d RSS失败，错误码{code}, 错误信息{out}")



