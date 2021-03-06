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


class GetLargeScreenDataRequest(JDCloudRequest):
    """
    根据区域、行业、一级指标、二级指标、起始时间等条件查询数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetLargeScreenDataRequest, self).__init__(
            '/regions/{regionId}/getData', 'GET', header, version)
        self.parameters = parameters


class GetLargeScreenDataParameters(object):

    def __init__(self, regionId, region, industry, startDate, endDate, firstIndex, ):
        """
        :param regionId: 地域ID
        :param region: 查询区域，比如某某省或某某市（可选区域以最终授权为准）
        :param industry: 查询行业，比如某个水果或者农作物（可选行业以最终授权为准）
        :param startDate: 查询起始时间，格式如下：yyyy-MM-dd
        :param endDate: 查询结束时间，格式如下：yyyy-MM-dd
        :param firstIndex: 数据对应的第一级分析指标（可选一级指标以最终授权为准）
        """

        self.regionId = regionId
        self.region = region
        self.industry = industry
        self.startDate = startDate
        self.endDate = endDate
        self.firstIndex = firstIndex
        self.secondIndex = None

    def setSecondIndex(self, secondIndex):
        """
        :param secondIndex: (Optional) 数据对应的第二级分析指标，如不填写，则默认把一级指标下的所有二级指标都查询出来（可选二级指标以最终授权为准）
        """
        self.secondIndex = secondIndex

