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


class UpdateFunctionRequest(JDCloudRequest):
    """
    更新函数
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateFunctionRequest, self).__init__(
            '/regions/{regionId}/functions/{functionName}', 'PUT', header, version)
        self.parameters = parameters


class UpdateFunctionParameters(object):

    def __init__(self, regionId, functionName, description, entrance, memory, runTime, overTime, code, environment, logSetId, logTopicId, vpcId, subnetId):
        """
        :param regionId: Region ID
        :param functionName: 函数名称
        :param description: 函数描述信息
        :param entrance: 函数入口，格式为入口文件.入口函数名
        :param memory: 函数运行最大内存
        :param runTime: 函数运行环境
        :param overTime: 函数运行超时时间
        :param code: 函数代码包
        :param environment: 函数运行时环境变量
        :param logSetId: 函数指定的日志集Id
        :param logTopicId: 函数指定的日志主题Id
        :param vpcId: 函数配置的VPCId
        :param subnetId: 函数配置的子网Id
        """

        self.regionId = regionId
        self.functionName = functionName
        self.description = description
        self.entrance = entrance
        self.memory = memory
        self.runTime = runTime
        self.overTime = overTime
        self.version = None
        self.code = code
        self.environment = environment
        self.logSetId = logSetId
        self.logTopicId = logTopicId
        self.vpcId = vpcId
        self.subnetId = subnetId

    def setVersion(self, version):
        """
        :param version: (Optional) 函数版本
        """
        self.version = version
