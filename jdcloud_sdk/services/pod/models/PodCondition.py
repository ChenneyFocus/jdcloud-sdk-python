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


class PodCondition(object):

    def __init__(self, lastProbeTime=None, lastTransitionTime=None, reason=None, status=None, message=None, conditionType=None):
        """
        :param lastProbeTime: (Optional) 最后一次探测状态的时间
        :param lastTransitionTime: (Optional) 最后一次改变状态的时间
        :param reason: (Optional) 最后一次状态改变的简要原因
        :param status: (Optional) Status is the status of the condition. Can be True, False, Unknown.
        :param message: (Optional) 最后一次状态改变的信息
        :param conditionType: (Optional) 状态的条件。目前仅限 Ready.
        """

        self.lastProbeTime = lastProbeTime
        self.lastTransitionTime = lastTransitionTime
        self.reason = reason
        self.status = status
        self.message = message
        self.conditionType = conditionType
