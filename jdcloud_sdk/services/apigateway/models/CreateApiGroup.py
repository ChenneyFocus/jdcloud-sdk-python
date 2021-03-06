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


class CreateApiGroup(object):

    def __init__(self, groupName, authType, description=None, prefix=None, keyCheck=None, prefixStrip=None, groupType=None, jdsfName=None, jdsfRegistryName=None, jdsfId=None):
        """
        :param groupName:  名称
        :param description: (Optional) 描述
        :param prefix: (Optional) 分组路径前缀，无需添加/
        :param keyCheck: (Optional) 密钥验证方式：check_exist（密钥必须在访问授权中已配置）、no_check_exist（无需事先配置）
        :param authType:  访问授权方式：None（免鉴权）、jd_cloud（开启访问授权，且必须使用京东云的AK、SK验签）、hufu（虎符用户）
        :param prefixStrip: (Optional) 是否转发分组路径到后端服务：0（不转发）、1（转发）默认为1
        :param groupType: (Optional) 分组类型：api_group（api分组）、jdsf_group（微服务分组）默认为 api_group
        :param jdsfName: (Optional) 微服务网关名称
        :param jdsfRegistryName: (Optional) 微服务注册中心ID
        :param jdsfId: (Optional) 微服务网关ID
        """

        self.groupName = groupName
        self.description = description
        self.prefix = prefix
        self.keyCheck = keyCheck
        self.authType = authType
        self.prefixStrip = prefixStrip
        self.groupType = groupType
        self.jdsfName = jdsfName
        self.jdsfRegistryName = jdsfRegistryName
        self.jdsfId = jdsfId
