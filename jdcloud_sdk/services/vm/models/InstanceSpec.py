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


class InstanceSpec(object):

    def __init__(self, az, instanceType, imageId, name, primaryNetworkInterface, systemDisk, password=None, keyNames=None, elasticIp=None, dataDisks=None, charge=None, description=None):
        """
        :param az:  实例所属的可用区
        :param instanceType:  实例类型
        :param imageId:  镜像ID
        :param name:  主机名称，不为空且只允许中文、数字、大小写字母、英文下划线“_”及中划线“-”，不超过32字符
        :param password: (Optional) "密码，长度8-30个字符"
"a)不能出现的字符或完整单词，如下：jd、JD、360、bug、BUG、com、COM、cloud、CLOUD、password、PASSWORD"
"b)不能出现连续三位及三位以上数字，例：123、987"
"c)不能出现连续三位及三位以上的字母，例：abc、CBA、bcde、cdef"
"d)不能出现三位及三位以上键位顺序（仅包括字母），例：qaz、tfc、wsx、xsw、qwert、trewq"
"e)密码中不能出现自己的用户名"
"g)至少同时包含三类（大写字母，小写字母，数字和特殊字符，特殊字符为 ** ()`~!@#$%&_-+={}[]:\";'<>,.?/）*|"

        :param keyNames: (Optional) 密钥对名称
        :param elasticIp: (Optional) 主网卡主IP关联的弹性IP规格
        :param primaryNetworkInterface:  主网卡配置信息
        :param systemDisk:  系统盘配置信息
        :param dataDisks: (Optional) 数据盘配置信息
        :param charge: (Optional) 计费配置
        :param description: (Optional) 主机描述，长度不超过256字符
        """

        self.az = az
        self.instanceType = instanceType
        self.imageId = imageId
        self.name = name
        self.password = password
        self.keyNames = keyNames
        self.elasticIp = elasticIp
        self.primaryNetworkInterface = primaryNetworkInterface
        self.systemDisk = systemDisk
        self.dataDisks = dataDisks
        self.charge = charge
        self.description = description
