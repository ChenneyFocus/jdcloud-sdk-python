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


class CacheInstanceSpec(object):

    def __init__(self, vpcId, subnetId, cacheInstanceName, cacheInstanceClass, azId, password=None, cacheInstanceDescription=None):
        """
        :param vpcId:  缓存redis实例所属的私有网络ID
        :param subnetId:  缓存redis实例在私有网络下所属的子网ID
        :param cacheInstanceName:  缓存redis实例名称，只支持数字、字母、英文下划线、中文，且不少于2字符不超过32字符
        :param cacheInstanceClass:  缓存redis实例规格代码，参见实例规格代码表<a href="https://www.jdcloud.com/help/detail/411/isCatalog/1">实例规格代码</a>。
        :param password: (Optional) 密码，为空即为免密，包含且只支持字母及数字，不少于8字符不超过16字符
        :param azId:  缓存Redis实例所在区域可用区ID信息
        :param cacheInstanceDescription: (Optional) 缓存Redis实例描述，不能超过256个字符
        """

        self.vpcId = vpcId
        self.subnetId = subnetId
        self.cacheInstanceName = cacheInstanceName
        self.cacheInstanceClass = cacheInstanceClass
        self.password = password
        self.azId = azId
        self.cacheInstanceDescription = cacheInstanceDescription
