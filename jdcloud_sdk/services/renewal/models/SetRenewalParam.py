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

    def __init__(self, instanceIds, autoRenewStatus, appCode, serviceCode, timeSpan=None, timeUnit=None, allAutoPay=None):
        """
        :param instanceIds:  资源id列表,英文逗号分隔
        :param autoRenewStatus:  自动续费状态 0-关闭自动续费,1-开通或修改自动续费
        :param appCode:  业务线
        :param serviceCode:  产品线
        :param timeSpan: (Optional) 续费周期（autoRenewStatus=1时必传）
        :param timeUnit: (Optional) 时间单位 1-小时 2-天 3-月 4-年（autoRenewStatus=1时必传）
        :param allAutoPay: (Optional) 是否绑定关联资源一并续费 0-不绑定,1-绑定（autoRenewStatus=1时必传）
        """

        self.instanceIds = instanceIds
        self.autoRenewStatus = autoRenewStatus
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.allAutoPay = allAutoPay
