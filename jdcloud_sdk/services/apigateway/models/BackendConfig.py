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


class BackendConfig(object):

    def __init__(self, environment, backendServiceType, sort, backendConfigId=None, baseGroupId=None, backendUrl=None, headerParams=None, queryParams=None, description=None, createTime=None, userSort=None, jdsfId=None, jdsfParam=None, jdsfRegion=None, jdsfPin=None):
        """
        :param backendConfigId: (Optional) 接口ID
        :param baseGroupId: (Optional) 分组ID
        :param environment:  环境：test、preview、online
        :param backendUrl: (Optional) 后端地址
        :param backendServiceType:  后端服务类型：mock、HTTP/HTTPS
        :param headerParams: (Optional) header参数列表
        :param queryParams: (Optional) query参数列表
        :param description: (Optional) 描述
        :param createTime: (Optional) 发布日期，格式为毫秒级时间戳
        :param sort:  排序，赋值0时为默认的后端配置
        :param userSort: (Optional) 排序，用于展示使用
        :param jdsfId: (Optional) vpc网关id
        :param jdsfParam: (Optional) vpc后端地址
        :param jdsfRegion: (Optional) vpc网关所属region
        :param jdsfPin: (Optional) vpc网关创建者的pin
        """

        self.backendConfigId = backendConfigId
        self.baseGroupId = baseGroupId
        self.environment = environment
        self.backendUrl = backendUrl
        self.backendServiceType = backendServiceType
        self.headerParams = headerParams
        self.queryParams = queryParams
        self.description = description
        self.createTime = createTime
        self.sort = sort
        self.userSort = userSort
        self.jdsfId = jdsfId
        self.jdsfParam = jdsfParam
        self.jdsfRegion = jdsfRegion
        self.jdsfPin = jdsfPin