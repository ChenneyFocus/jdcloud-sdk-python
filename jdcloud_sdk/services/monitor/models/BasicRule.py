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


class BasicRule(object):

    def __init__(self, calculation, metric, operation, period, threshold, times, downSample=None, noticeLevel=None):
        """
        :param calculation:  统计方法，必须与定义的metric一致，可选值列表：avg,sum,max,min
        :param downSample: (Optional) 降采样函数
        :param metric:  监控项唯一标识，可根据DescribeMetricsForCreateAlarm接口查询各产品线可用的监控项（创建规则时使用Metric字段）。格式：metric:downsample
        :param noticeLevel: (Optional) 
        :param operation:  报警比较符，只能为以下几种lte(<=),lt(<),gt(>),gte(>=),eq(==),ne(!=)
        :param period:  查询指标的周期，单位为分钟,目前支持的取值：1,2，5，10,15，30，60
        :param threshold:  报警阈值，目前只开放数值类型功能
        :param times:  连续探测几次都满足阈值条件时报警，可选值:1,2,3,5,10,15,30,60
        """

        self.calculation = calculation
        self.downSample = downSample
        self.metric = metric
        self.noticeLevel = noticeLevel
        self.operation = operation
        self.period = period
        self.threshold = threshold
        self.times = times
