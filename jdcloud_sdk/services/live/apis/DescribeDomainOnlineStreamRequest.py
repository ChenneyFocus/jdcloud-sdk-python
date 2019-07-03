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


class DescribeDomainOnlineStreamRequest(JDCloudRequest):
    """
    查询在线流列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDomainOnlineStreamRequest, self).__init__(
            '/describeDomainOnlineStream', 'GET', header, version)
        self.parameters = parameters


class DescribeDomainOnlineStreamParameters(object):

    def __init__(self, domainName, startTime, ):
        """
        :param domainName: 推流域名
        :param startTime: 起始时间
- UTC时间
  格式:yyyy-MM-dd'T'HH:mm:ss'Z'
  示例:2018-10-21T10:00:00Z

        """

        self.domainName = domainName
        self.appName = None
        self.streamName = None
        self.pageNum = None
        self.pageSize = None
        self.startTime = startTime
        self.endTime = None

    def setAppName(self, appName):
        """
        :param appName: (Optional) 应用名称
        """
        self.appName = appName

    def setStreamName(self, streamName):
        """
        :param streamName: (Optional) 流名称
        """
        self.streamName = streamName

    def setPageNum(self, pageNum):
        """
        :param pageNum: (Optional) 页码，起始页码1

        """
        self.pageNum = pageNum

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页最大记录数，取值：[10,100]，默认：10

        """
        self.pageSize = pageSize

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间:
- UTC时间
  格式:yyyy-MM-dd'T'HH:mm:ss'Z'
  示例:2018-10-21T10:00:00Z
- 为空,默认为当前时间，查询时间跨度不超过30天

        """
        self.endTime = endTime

