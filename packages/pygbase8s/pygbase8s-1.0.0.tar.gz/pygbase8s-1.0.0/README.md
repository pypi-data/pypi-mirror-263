# pygbase8s

#### 介绍
提供gbase8s数据库及相关产品的安装部署、实例、集群配置等功能


#### 安装教程

pip install pygbase8s

#### 使用说明


```python
from pygbase8s import RemoteMachine
# 创建一个服务器实例
machine = RemoteMachine(ip='xxx.xxx.xxx.xxx', password='root_password')

from pygbase8s import IDS
# 指定数据库目录
ids = IDS(path="/opt/gbase8s", machine=machine)
# 安装数据库  
ids.install(pkg_path="/data/GBase8sxxx.tar")

from pygbase8s import ServerPool
# 初始化实例池
pool = ServerPool(ids=ids, count=5)
pool.initialize()
# 从实例池获取一个实例并初始化
server = pool.get_server()
server.initialize()
# 从实例池获取一个SDS集群并初始化
cluster = pool.get_cluster("sds")
cluster.initialize()
# 给集群配置CM
from pygbase8s import CM
from pygbase8s import CSDK
csdk = CSDK(path="/opt/gbase8s", machine=machine)
csdk.install('/data/ClientSDKxxx.tar')
cm = CM(csdk=csdk, cluster=cluster)
cm.startup()
```


#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
