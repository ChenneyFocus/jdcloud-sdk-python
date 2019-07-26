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


class DiskSpec(object):

    def __init__(self, az, name, diskType, diskSizeGB, description=None, iops=None, snapshotId=None, charge=None, multiAttachable=None, encrypt=None):
        """
        :param az:  云硬盘所属的可用区
        :param name:  云硬盘名称
        :param description: (Optional) 云硬盘描述
        :param diskType:  云硬盘类型，取值为ssd、premium-hdd、ssd.gp1、ssd.io1、hdd.std1之一
        :param diskSizeGB:  云硬盘大小，单位为 GiB，ssd 类型取值范围[20,1000]GB，步长为10G，premium-hdd 类型取值范围[20,3000]GB，步长为10G, ssd.gp1, ssd.io1, hdd.std1 类型取值均是范围[20,16000]GB，步长为10G
        :param iops: (Optional) 云硬盘IOPS的大小，当且仅当云盘类型是ssd.io1型的云盘有效，步长是10.
        :param snapshotId: (Optional) 用于创建云硬盘的快照ID
        :param charge: (Optional) 计费配置；如不指定，默认计费类型是后付费-按使用时常付费
        :param multiAttachable: (Optional) 云硬盘是否支持一盘多主机挂载，默认为false（不支持）
        :param encrypt: (Optional) 云硬盘是否加密，默认为false（不加密）
        """

        self.az = az
        self.name = name
        self.description = description
        self.diskType = diskType
        self.diskSizeGB = diskSizeGB
        self.iops = iops
        self.snapshotId = snapshotId
        self.charge = charge
        self.multiAttachable = multiAttachable
        self.encrypt = encrypt
