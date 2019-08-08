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


class MonitorAlarmInfo(object):

    def __init__(self, domainId=None, subDomainName=None, host=None, id=None, startTime=None, endTime=None):
        """
        :param domainId: (Optional) 域名ID
        :param subDomainName: (Optional) 子域名
        :param host: (Optional) 故障IP/域名
        :param id: (Optional) null
        :param startTime: (Optional) 故障开始时间，格式Unix timestamp，时间单位：毫秒
        :param endTime: (Optional) 故障结束时间，格式Unix timestamp，时间单位：毫秒
        """

        self.domainId = domainId
        self.subDomainName = subDomainName
        self.host = host
        self.id = id
        self.startTime = startTime
        self.endTime = endTime
