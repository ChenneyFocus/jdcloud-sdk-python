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


class QuerywafBlackRulesRequest(JDCloudRequest):
    """
    查询WAF黑名单规则列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QuerywafBlackRulesRequest, self).__init__(
            '/domain/{domain}/wafBlackRules', 'GET', header, version)
        self.parameters = parameters


class QuerywafBlackRulesParameters(object):

    def __init__(self, domain, ruleType, ):
        """
        :param domain: 用户域名
        :param ruleType: ruleType, valid values [ip, geo, uri]
        """

        self.domain = domain
        self.ruleType = ruleType
        self.id = None
        self.pageSize = None
        self.pageIndex = None

    def setId(self, id):
        """
        :param id: (Optional) ruleId, defalut empty
        """
        self.id = id

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) page size , default 0 to query all
        """
        self.pageSize = pageSize

    def setPageIndex(self, pageIndex):
        """
        :param pageIndex: (Optional) page index , default 0 to query all
        """
        self.pageIndex = pageIndex

