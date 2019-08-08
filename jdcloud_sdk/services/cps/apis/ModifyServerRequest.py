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


class ModifyServerRequest(JDCloudRequest):
    """
    修改后端服务器
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyServerRequest, self).__init__(
            '/regions/{regionId}/serverGroups/{serverGroupId}/servers/{serverId}', 'POST', header, version)
        self.parameters = parameters


class ModifyServerParameters(object):

    def __init__(self, regionId, serverGroupId, serverId, ):
        """
        :param regionId: 地域ID，可调用接口（describeRegiones）获取云物理服务器支持的地域
        :param serverGroupId: 服务器组ID
        :param serverId: 后端服务器ID
        """

        self.regionId = regionId
        self.serverGroupId = serverGroupId
        self.serverId = serverId
        self.weight = None

    def setWeight(self, weight):
        """
        :param weight: (Optional) 权重
        """
        self.weight = weight

