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


class QueryTemplateListRequest(JDCloudRequest):
    """
    查询富媒体短信内容列表接口
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(QueryTemplateListRequest, self).__init__(
            '/regions/{regionId}/queryTemplateList', 'POST', header, version)
        self.parameters = parameters


class QueryTemplateListParameters(object):

    def __init__(self, regionId, appId, pageNum, pageLimit, ):
        """
        :param regionId: Region ID
        :param appId: 应用ID
        :param pageNum: 第几页
        :param pageLimit: 每页多少条记录
        """

        self.regionId = regionId
        self.appId = appId
        self.title = None
        self.pageNum = pageNum
        self.pageLimit = pageLimit
        self.status = None
        self.startTime = None
        self.endTime = None

    def setTitle(self, title):
        """
        :param title: (Optional) 查询标题关键词
        """
        self.title = title

    def setStatus(self, status):
        """
        :param status: (Optional) 审核状态：0: 审核中 1: 通过 2: 未通过 4:待提交
        """
        self.status = status

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 开始时间,格式YYYY-MM-DD
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间,格式YYYY-MM-DD
        """
        self.endTime = endTime

