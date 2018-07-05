# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class SetCleanThresholdRequest(JDCloudRequest):
    """
    设置公网Ip的清洗阈值
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetCleanThresholdRequest, self).__init__(
            '/regions/{regionId}/ipResources/{ip}:setCleanThreshold', 'POST', header, version)
        self.parameters = parameters


class SetCleanThresholdParameters(object):

    def __init__(self, regionId, ip, cleanThresholdSpec):
        """
        :param regionId: Region ID
        :param ip: 公网ip
        :param cleanThresholdSpec: cc参数
        """

        self.regionId = regionId
        self.ip = ip
        self.cleanThresholdSpec = cleanThresholdSpec
