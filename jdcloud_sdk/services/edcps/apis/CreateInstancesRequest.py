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
    创建一台或多台指定配置的分布式云物理服务器<br/>
- 地域与可用区<br/>
  - 调用接口（queryEdCPSRegions）获取分布式云物理服务器支持的地域与可用区<br/>
- 实例类型<br/>
  - 调用接口（describeDeviceTypes）获取物理实例类型列表<br/>
  - 不能使用已下线、或已售馨的实例类型<br/>
- 操作系统<br/>
  - 可调用接口（describeOS）获取分布式云物理服务器支持的操作系统列表<br/>
- 存储<br/>
  - 数据盘多种RAID可选，可调用接口（describeDeviceRaids）获取服务器支持的RAID列表<br/>
- 网络<br/>
  - 网络类型目前支持vpc<br/>
  - 线路目前支持联通un、电信ct、移动cm<br/>
  - 支持不启用外网，如果启用外网，带宽范围[1,200] 单位Mbps<br/>
- 其他<br/>
  - 购买时长，可按年或月购买：月取值范围[1,9], 年取值范围[1,3]<br/>
  - 密码设置参考公共参数规范<br/>

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateInstancesRequest, self).__init__(
            '/regions/{regionId}/instances', 'PUT', header, version)
        self.parameters = parameters


class CreateInstancesParameters(object):

    def __init__(self, regionId, instanceSpec):
        """
        :param regionId: 地域ID，可调用接口（describeEdCPSRegions）获取分布式云物理服务器支持的地域
        :param instanceSpec: 描述分布式云物理服务器配置
        """

        self.regionId = regionId
        self.clientToken = None
        self.instanceSpec = instanceSpec

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 由客户端生成，用于保证请求的幂等性，长度不能超过36个字符；<br/>
如果多个请求使用了相同的clientToken，只会执行第一个请求，之后的请求直接返回第一个请求的结果<br/>

        """
        self.clientToken = clientToken
