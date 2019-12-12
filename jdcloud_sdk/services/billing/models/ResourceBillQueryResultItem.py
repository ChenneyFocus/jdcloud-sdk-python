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


class ResourceBillQueryResultItem(object):

    def __init__(self, billId=None, pin=None, appCode=None, serviceCode=None, serviceCodeName=None, billingType=None, billingTypeName=None, resourceId=None, region=None, regionName=None, billStartTime=None, billEndTime=None, startTime=None, endTime=None, totalFee=None, cashPayFee=None, cashCouponPayFee=None, balancePayFee=None, arrearFee=None, timeSpan=None, timeUnit=None, opTypeName=None, timeSpanName=None, timeUnitName=None, settleTime=None, systemType=None, resourceName=None, tagDetails=None):
        """
        :param billId: (Optional) 账单id
        :param pin: (Optional) 用户pin
        :param appCode: (Optional) appCode
        :param serviceCode: (Optional) serviceCode
        :param serviceCodeName: (Optional) serviceCodeName
        :param billingType: (Optional) 计费类型
        :param billingTypeName: (Optional) 计费类型描述
        :param resourceId: (Optional) 资源id
        :param region: (Optional) 区域
        :param regionName: (Optional) 区域名称
        :param billStartTime: (Optional) 账单开始时间
        :param billEndTime: (Optional) 账单结束时间
        :param startTime: (Optional) 开始时间
        :param endTime: (Optional) 结束时间
        :param totalFee: (Optional) 总金额
        :param cashPayFee: (Optional) 现金支付金额
        :param cashCouponPayFee: (Optional) 代金券支付金额
        :param balancePayFee: (Optional) 余额支付金额
        :param arrearFee: (Optional) 欠费金额
        :param timeSpan: (Optional) 时间
        :param timeUnit: (Optional) 时间单位
        :param opTypeName: (Optional) 1：新购 2：续费 3：配置变更
        :param timeSpanName: (Optional) 时间
        :param timeUnitName: (Optional) 时间单位名称 1：小时 2：天 3：月 4：年
        :param settleTime: (Optional) 结算日期
        :param systemType: (Optional) 1：老计费 2：新计费
        :param resourceName: (Optional) 资源名称
        :param tagDetails: (Optional) 标签明细
        """

        self.billId = billId
        self.pin = pin
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.serviceCodeName = serviceCodeName
        self.billingType = billingType
        self.billingTypeName = billingTypeName
        self.resourceId = resourceId
        self.region = region
        self.regionName = regionName
        self.billStartTime = billStartTime
        self.billEndTime = billEndTime
        self.startTime = startTime
        self.endTime = endTime
        self.totalFee = totalFee
        self.cashPayFee = cashPayFee
        self.cashCouponPayFee = cashCouponPayFee
        self.balancePayFee = balancePayFee
        self.arrearFee = arrearFee
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.opTypeName = opTypeName
        self.timeSpanName = timeSpanName
        self.timeUnitName = timeUnitName
        self.settleTime = settleTime
        self.systemType = systemType
        self.resourceName = resourceName
        self.tagDetails = tagDetails
