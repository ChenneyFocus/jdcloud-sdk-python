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


class DescribeActiveQueryPerformanceRequest(JDCloudRequest):
    """
    根据用户定义的查询条件，获取正在执行中的SQL执行的性能信息。用户可以根据这些信息查找与SQL执行相关的性能瓶颈，并进行优化。<br>- 仅支持SQL Server
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeActiveQueryPerformanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/performance:describeActiveQueryPerformance', 'GET', header, version)
        self.parameters = parameters


class DescribeActiveQueryPerformanceParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.db = None
        self.threshold = None
        self.pageNumber = None
        self.pageSize = None

    def setDb(self, db):
        """
        :param db: (Optional) 需要查询的数据库名，多个数据库名之间用英文逗号分隔，默认所有数据库
        """
        self.db = db

    def setThreshold(self, threshold):
        """
        :param threshold: (Optional) 返回执行时间大于等于threshold的记录，默认10，单位秒
        """
        self.threshold = threshold

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，默认为1，取值范围：[-1,1000)。pageNumber为-1时，返回所有数据页码；超过总页数时，显示最后一页。
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为50，取值范围：[1,100]，只能为10的倍数
        """
        self.pageSize = pageSize
