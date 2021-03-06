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


class CreateInstancesRequest(JDCloudRequest):
    """
    创建一台或多台指定配置的云主机，创建模式分为三种：1.普通方式、2.使用高可用组、3.使用启动模板。三种方式创建云主机时参数的必传与非必传是不同的，具体请参考<a href="http://docs.jdcloud.com/virtual-machines/api/create_vm_sample">参数详细说明</a><br>
- 创建云主机需要通过实名认证
- 实例规格
    - 可查询<a href="http://docs.jdcloud.com/virtual-machines/api/describeinstancetypes">DescribeInstanceTypes</a>接口获得指定地域或可用区的规格信息。
    - 不能使用已下线、或已售馨的规格ID
- 镜像
    - Windows Server所有镜像CPU不可选超过64核CPU。
    - 可查询<a href="http://docs.jdcloud.com/virtual-machines/api/describeimages">DescribeImages</a>接口获得指定地域的镜像信息。
    - 选择的镜像必须支持选择的实例规格。可查询<a href="http://docs.jdcloud.com/virtual-machines/api/describeimageconstraints">DescribeImageConstraints</a>接口获得指定镜像的实例规格限制信息。<br>
- 网络配置
    - 指定主网卡配置信息
        - 必须指定subnetId
        - 可以指定elasticIp规格来约束创建的弹性IP，带宽取值范围[1-200]Mbps，步进1Mbps
        - 可以指定主网卡的内网主IP(primaryIpAddress)，此时maxCount只能为1
        - 安全组securityGroup需与子网Subnet在同一个私有网络VPC内
        - 一台云主机创建时必须至少指定一个安全组，至多指定5个安全组，如果没有指定安全组，默认使用默认安全组
        - 主网卡deviceIndex设置为1
- 存储
    - 系统盘
        - 磁盘分类，系统盘支持local或cloud
        - 磁盘大小
            - local：不能指定大小，默认为40GB
            - cloud：取值范围: 40-500GB，并且不能小于镜像的最小系统盘大小，如果没有指定，默认以镜像中的系统盘大小为准
        - 自动删除
            - 如果是local类型，默认自动删除，不可修改
            - 如果是cloud类型的按配置计费的云硬盘，默认为True，可修改
            - 如果是cloud类型的包年包月的云硬盘，默认为False，不可修改
    - 数据盘
        - 磁盘分类，数据盘仅支持cloud
        - 云硬盘类型可以选择ssd、premium-hdd、hdd.std1、ssd.gp1、ssd.io1
        - 磁盘大小
            - premium-hdd：范围[20,3000]GB，步长为10G
            - ssd：范围[20,1000]GB，步长为10G
            - hdd.std1、ssd.gp1、ssd.io1: 范围[20-16000]GB，步长为10GB
        - 自动删除
            - 默认自动删除，如果是包年包月的云硬盘，此参数不生效
        - 可以从快照创建磁盘
    - local类型系统的云主机可以挂载8块云硬盘
    - cloud类型系统的云主机可以挂载7块云硬盘
- 计费
    - 弹性IP的计费模式，如果选择按用量类型可以单独设置，其它计费模式都以主机为准
    - 云硬盘的计费模式以主机为准
- 其他
    - 创建完成后，主机状态为running
    - 仅Linux系统云主机可以指定密钥
    - maxCount为最大努力，不保证一定能达到maxCount
    - 虚机的az会覆盖磁盘的az属性
- 密码
    - <a href="http://docs.jdcloud.com/virtual-machines/api/general_parameters">参考公共参数规范</a>

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateInstancesRequest, self).__init__(
            '/regions/{regionId}/instances', 'POST', header, version)
        self.parameters = parameters


class CreateInstancesParameters(object):

    def __init__(self, regionId, instanceSpec, ):
        """
        :param regionId: 地域ID
        :param instanceSpec: 描述云主机配置

        """

        self.regionId = regionId
        self.instanceSpec = instanceSpec
        self.maxCount = None
        self.clientToken = None

    def setMaxCount(self, maxCount):
        """
        :param maxCount: (Optional) 购买云主机的数量；取值范围：[1,100]，默认为1。

        """
        self.maxCount = maxCount

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 用于保证请求的幂等性。由客户端生成，长度不能超过64个字符。

        """
        self.clientToken = clientToken

