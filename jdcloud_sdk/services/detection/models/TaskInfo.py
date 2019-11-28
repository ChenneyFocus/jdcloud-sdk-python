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


class TaskInfo(object):

    def __init__(self, abnormalCount=None, address=None, deleted=None, enabled=None, name=None, probeAvailability=None, probeCount=None, probeType=None, responseTime=None, taskId=None):
        """
        :param abnormalCount: (Optional) 探测异常数  ，null代表缺值。只统计探测失败，超时的个数。
        :param address: (Optional) task的探测地址
        :param deleted: (Optional) 该task状态[true:被删除]
        :param enabled: (Optional) 任务状态[false：己禁用，true：己启用]
        :param name: (Optional) task名称
        :param probeAvailability: (Optional) task的可用率
        :param probeCount: (Optional) 该task的探测源个数
        :param probeType: (Optional) task的探测类型，1：http，2：telnet
        :param responseTime: (Optional) task的探测平均响应时间
        :param taskId: (Optional) task的id
        """

        self.abnormalCount = abnormalCount
        self.address = address
        self.deleted = deleted
        self.enabled = enabled
        self.name = name
        self.probeAvailability = probeAvailability
        self.probeCount = probeCount
        self.probeType = probeType
        self.responseTime = responseTime
        self.taskId = taskId
