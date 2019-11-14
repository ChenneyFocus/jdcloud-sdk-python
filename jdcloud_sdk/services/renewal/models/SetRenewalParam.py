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


class SetRenewalParam(object):

    def __init__(self, appCode, serviceCode, instanceIds, autoRenewStatus, timeSpan=None, timeUnit=None, allAutoPay=None):
        """
        :param appCode:  业务线
        :param serviceCode:  产品线
        :param timeSpan: (Optional) 续费时长
        :param timeUnit: (Optional) 时间单位(MONTH-月,YEAR-年)
        :param instanceIds:  资源ID列表,英文逗号分隔
        :param autoRenewStatus:  自动续费状态(OPEN-开通自动续费,CLOSE-关闭自动续费,MODIFY-修改自动续费)
        :param allAutoPay: (Optional) 是否绑定关联资源一并开通自动续费(UNBIND：不绑定，BIND：绑定)
        """

        self.appCode = appCode
        self.serviceCode = serviceCode
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.instanceIds = instanceIds
        self.autoRenewStatus = autoRenewStatus
        self.allAutoPay = allAutoPay
