# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class RebuildContainerRequest(JDCloudRequest):
    """
    重置原生容器，对已有原生容器使用新的镜像重置。
原容器 id 不变，不涉及计费变动，暂不支持修改实例类型，不会改变原生容器所在的物理节点，也不支持修改已经使用的系统盘和数据盘以及网络相关参数。
- 镜像
    - 容器的镜像通过镜像名称来确定
    - nginx:tag 或 mysql/mysql-server:tag 这样命名的镜像表示 docker hub 官方镜像
    - container-registry/image:tag 这样命名的镜像表示私有仓储的镜像
    - 私有仓储必须兼容 docker registry 认证机制，并通过 secret 来保存机密信息
- 其他
    - rebuild 之前容器必须处于关闭状态
    - rebuild 完成后，容器仍为关闭状态

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RebuildContainerRequest, self).__init__(
            '/regions/{regionId}/containers/{containerId}:rebuild', 'POST', header, version)
        self.parameters = parameters


class RebuildContainerParameters(object):

    def __init__(self, regionId, containerId, ):
        """
        :param regionId: Region ID
        :param containerId: Container ID
        """

        self.regionId = regionId
        self.containerId = containerId
        self.image = None
        self.secret = None
        self.command = None
        self.args = None
        self.tty = None
        self.workingDir = None
        self.evns = None

    def setImage(self, image):
        """
        :param image: (Optional) 镜像名称 </br> 1. Docker Hub官方镜像通过类似nginx, mysql/mysql-server的名字指定 </br> </br> repository长度最大256个字符，tag最大128个字符，registry最大255个字符 </br> 下载镜像超时时间：10分钟
        """
        self.image = image

    def setSecret(self, secret):
        """
        :param secret: (Optional) secret引用名称；使用Docker Hub和京东云CR的镜像不需要secret
        """
        self.secret = secret

    def setCommand(self, command):
        """
        :param command: (Optional) 容器执行命令，如果不指定默认是docker镜像的ENTRYPOINT
        """
        self.command = command

    def setArgs(self, args):
        """
        :param args: (Optional) 容器执行命令的参数，如果不指定默认是docker镜像的CMD
        """
        self.args = args

    def setTty(self, tty):
        """
        :param tty: (Optional) 容器是否分配tty。默认不分配
        """
        self.tty = tty

    def setWorkingDir(self, workingDir):
        """
        :param workingDir: (Optional) 容器的工作目录。如果不指定，默认是根目录（/）；必须是绝对路径
        """
        self.workingDir = workingDir

    def setEvns(self, evns):
        """
        :param evns: (Optional) 容器执行的环境变量；如果和镜像中的环境变量Key相同，会覆盖镜像中的值；</br> 最大10对
        """
        self.evns = evns
