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


class PushStreamInfoItem(object):

    def __init__(self, app=None, stream=None, clientIp=None, nodeIp=None, startTime=None, endTime=None, duration=None):
        """
        :param app: (Optional) 
        :param stream: (Optional) 
        :param clientIp: (Optional) 
        :param nodeIp: (Optional) 
        :param startTime: (Optional) 任务创建时间,UTC时间
        :param endTime: (Optional) 任务创建时间,UTC时间
        :param duration: (Optional) 
        """

        self.app = app
        self.stream = stream
        self.clientIp = clientIp
        self.nodeIp = nodeIp
        self.startTime = startTime
        self.endTime = endTime
        self.duration = duration
