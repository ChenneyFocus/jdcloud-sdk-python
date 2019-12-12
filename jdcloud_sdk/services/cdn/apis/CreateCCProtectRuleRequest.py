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


class CreateCCProtectRuleRequest(JDCloudRequest):
    """
    新增一条CC防护规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateCCProtectRuleRequest, self).__init__(
            '/domain/{domain}/ccProtectRule', 'POST', header, version)
        self.parameters = parameters


class CreateCCProtectRuleParameters(object):

    def __init__(self, domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.uri = None
        self.detectPeriod = None
        self.singleIpLimit = None
        self.blockType = None
        self.blockTime = None

    def setUri(self, uri):
        """
        :param uri: (Optional) null
        """
        self.uri = uri

    def setDetectPeriod(self, detectPeriod):
        """
        :param detectPeriod: (Optional) null
        """
        self.detectPeriod = detectPeriod

    def setSingleIpLimit(self, singleIpLimit):
        """
        :param singleIpLimit: (Optional) null
        """
        self.singleIpLimit = singleIpLimit

    def setBlockType(self, blockType):
        """
        :param blockType: (Optional) null
        """
        self.blockType = blockType

    def setBlockTime(self, blockTime):
        """
        :param blockTime: (Optional) null
        """
        self.blockTime = blockTime

