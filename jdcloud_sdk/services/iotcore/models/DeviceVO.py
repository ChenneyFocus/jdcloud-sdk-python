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


class DeviceVO(object):

    def __init__(self, deviceId=None, deviceName=None, parentId=None, deviceType=None, status=None, identifier=None, secret=None, description=None, activatedTime=None, lastConnectedTime=None, createdTime=None, updatedTime=None, productKey=None, productName=None, productSecret=None, model=None, manufacturer=None, dynamicRegister=None):
        """
        :param deviceId: (Optional) 设备ID
        :param deviceName: (Optional) 设备名称
        :param parentId: (Optional) 父级设备Id
        :param deviceType: (Optional) 设备类型，同产品类型，0-普通设备，1-网关，2-Edge
        :param status: (Optional) 设备状态，0-未激活，1-激活离线，2-激活在线
        :param identifier: (Optional) 设备标识符
        :param secret: (Optional) 设备秘钥
        :param description: (Optional) 设备描述
        :param activatedTime: (Optional) 激活时间
        :param lastConnectedTime: (Optional) 最后连接时间
        :param createdTime: (Optional) 注册时间
        :param updatedTime: (Optional) 修改时间
        :param productKey: (Optional) 产品Key
        :param productName: (Optional) 产品名称
        :param productSecret: (Optional) 产品秘钥
        :param model: (Optional) 设备型号
        :param manufacturer: (Optional) 设备厂商
        :param dynamicRegister: (Optional) 是否开启动态注册,0:关闭,1:开启，开启动态注册的设备认证类型为一型一密，否则为一机一密
        """

        self.deviceId = deviceId
        self.deviceName = deviceName
        self.parentId = parentId
        self.deviceType = deviceType
        self.status = status
        self.identifier = identifier
        self.secret = secret
        self.description = description
        self.activatedTime = activatedTime
        self.lastConnectedTime = lastConnectedTime
        self.createdTime = createdTime
        self.updatedTime = updatedTime
        self.productKey = productKey
        self.productName = productName
        self.productSecret = productSecret
        self.model = model
        self.manufacturer = manufacturer
        self.dynamicRegister = dynamicRegister
