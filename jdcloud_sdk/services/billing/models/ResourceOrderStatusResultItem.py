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


class ResourceOrderStatusResultItem(object):

    def __init__(self, resourceId=None, billingType=None, status=None, pin=None, region=None, updateTime=None):
        """
        :param resourceId: (Optional) 资源id
        :param billingType: (Optional) 计费类型 1:按配置 2:按用量 3:包年包月 4:一次性
        :param status: (Optional) 资源状态 1:正常 2:停服 3:删除
        :param pin: (Optional) 用户pin
        :param region: (Optional) 资源区域
        :param updateTime: (Optional) 操作时间
        """

        self.resourceId = resourceId
        self.billingType = billingType
        self.status = status
        self.pin = pin
        self.region = region
        self.updateTime = updateTime
