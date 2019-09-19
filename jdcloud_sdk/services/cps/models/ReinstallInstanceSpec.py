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


class ReinstallInstanceSpec(object):

    def __init__(self, az, imageType, osTypeId, sysRaidTypeId, keepData, dataRaidTypeId, password, hostname=None, userData=None, keypairId=None):
        """
        :param az:  可用区, 如cn-east-1a
        :param imageType:  镜像类型, 取值范围：standard、standard_app
        :param osTypeId:  操作系统类型ID
        :param sysRaidTypeId:  系统盘RAID类型ID
        :param keepData:  是否保留数据盘数据, 取值为：yes、no
        :param dataRaidTypeId:  数据盘RAID类型ID
        :param password:  密码
        :param hostname: (Optional) 主机名
        :param userData: (Optional) 可执行脚本Base64编码后的内容，支持shell和python脚本
        :param keypairId: (Optional) 秘钥对id
        """

        self.az = az
        self.imageType = imageType
        self.osTypeId = osTypeId
        self.sysRaidTypeId = sysRaidTypeId
        self.keepData = keepData
        self.dataRaidTypeId = dataRaidTypeId
        self.password = password
        self.hostname = hostname
        self.userData = userData
        self.keypairId = keypairId
