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

    def __init__(self, az, deviceType, imageType, osTypeId, sysRaidTypeId, dataRaidTypeId, networkType, name, count, charge, hostname=None, subnetId=None, enableInternet=None, cidr=None, privateIp=None, lineType=None, bandwidth=None, extraUplinkBandwidth=None, description=None, password=None, userData=None, keypairId=None, aliasIps=None):
        """
        :param az:  可用区, 如 cn-east-tz1
        :param deviceType:  实例类型, 如 edcps.c.normal1
        :param hostname: (Optional) 主机名
        :param imageType:  镜像类型, 取值范围：standard
        :param osTypeId:  操作系统类型ID
        :param sysRaidTypeId:  系统盘RAID类型ID
        :param dataRaidTypeId:  数据盘RAID类型ID
        :param subnetId: (Optional) 子网编号
        :param enableInternet: (Optional) 是否启用外网，取值范围：yes、no
        :param networkType:  网络类型，取值范围：vpc
        :param cidr: (Optional) 网络CIDR
        :param privateIp: (Optional) 内网IP
        :param lineType: (Optional) 外网链路类型, 目前支持联通un、电信ct、移动cm
        :param bandwidth: (Optional) 外网带宽, 范围[1,10240] 单位Mbps
        :param extraUplinkBandwidth: (Optional) 额外上行带宽, 范围[0,10240] 单位Mbps
        :param name:  云物理服务器名称
        :param description: (Optional) 云物理服务器描述
        :param password: (Optional) 密码，不传值会随机生成密码
        :param count:  购买数量
        :param userData: (Optional) 可执行脚本Base64编码后的内容，支持shell和python脚本
        :param keypairId: (Optional) 密钥对id
        :param charge:  计费配置
        :param aliasIps: (Optional) 别名ip配置
        """

        self.az = az
        self.deviceType = deviceType
        self.hostname = hostname
        self.imageType = imageType
        self.osTypeId = osTypeId
        self.sysRaidTypeId = sysRaidTypeId
        self.dataRaidTypeId = dataRaidTypeId
        self.subnetId = subnetId
        self.enableInternet = enableInternet
        self.networkType = networkType
        self.cidr = cidr
        self.privateIp = privateIp
        self.lineType = lineType
        self.bandwidth = bandwidth
        self.extraUplinkBandwidth = extraUplinkBandwidth
        self.name = name
        self.description = description
        self.password = password
        self.count = count
        self.userData = userData
        self.keypairId = keypairId
        self.charge = charge
        self.aliasIps = aliasIps
