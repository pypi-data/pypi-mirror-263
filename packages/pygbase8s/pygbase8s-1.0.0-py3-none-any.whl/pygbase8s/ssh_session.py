# coding: utf-8
# @Time    : 2024/2/28 12:16
# @Author  : wangwei
from pygbase8s.env import ENV

'''
ssh 连接
'''


class SSHSession:
    """
    在指定Machine上执行shell命令的连接类
    """
    def __init__(self, ssh):
        """
        :param ssh: paramiko.SSHClient
        """
        self.ssh = ssh
        self.env = ENV()
        self.char_set = 'utf8'
        self.ip = self.ssh.get_transport().sock.getpeername()[0]

    def run_cmd(self, cmd, cwd: str = None, username: str = None, timeout: int = None):
        """
        执行shell命令
        :param cmd: str， 命令字符串
        :param cwd: str, 工作路径
        :param username: str, 执行命令的用户
        :param timeout: int, 命令执行超时时间
        :return: code 命令状态码, out 标准输出+标准错误
        """
        cmds = [f"export {k}={v}" if v else f'unset {k}'for k, v in self.env.get_variables().items()]
        exec_cmd = cmd if timeout is None else f"timeout -s SIGKILL {timeout}s {cmd}"
        cmds.append(exec_cmd)
        cmds_str = ";".join(cmds)
        if cwd:
            cmds_str = f'cd {cwd}; {cmds_str}'
        if username:
            cmds_str = f'su - {username} --session-command "{cmds_str}"'
        stdin, stdout, stderr = self.ssh.exec_command(cmds_str, get_pty=True)
        return_code = stdout.channel.recv_exit_status()
        output = stdout.read().decode(self.char_set) + stderr.read().decode(self.char_set)
        return return_code, output

    def set_char_set(self, char_set):
        """
        设置字符集
        :param char_set: str, utf8、 gbk...
        :return:
        """
        self.char_set = char_set

    def get_char_set(self):
        """
        获取字符集
        :return: str
        """
        return self.char_set

    def close(self):
        """
        关闭连接
        :return:
        """
        self.ssh.close()
