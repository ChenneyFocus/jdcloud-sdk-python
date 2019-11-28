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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class TestSiteMonitorRequest(JDCloudRequest):
    """
    测试站点监控参数
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(TestSiteMonitorRequest, self).__init__(
            '/testSiteMonitor', 'POST', header, version)
        self.parameters = parameters


class TestSiteMonitorParameters(object):

    def __init__(self, address, cycle, name, source, taskType, ):
        """
        :param address: 地址
        :param cycle: 探测频率
        :param name: 任务名称
        :param source: 探测源
        :param taskType: 任务类型，可选值：HTTP、PING 、TCP 、UDP、DNS、SMTP、POP3和FTP
        """

        self.address = address
        self.advanceChecked = None
        self.createdTime = None
        self.cycle = cycle
        self.defaultSource = None
        self.dnsOption = None
        self.enabled = None
        self.ftpOption = None
        self.hawkeyeId = None
        self.httpOption = None
        self.id = None
        self.isDeleted = None
        self.name = name
        self.pin = None
        self.pingOption = None
        self.pop3Option = None
        self.port = None
        self.smtpOption = None
        self.source = source
        self.stats = None
        self.taskType = taskType
        self.tcpOption = None
        self.udpOption = None
        self.updatedTime = None

    def setAdvanceChecked(self, advanceChecked):
        """
        :param advanceChecked: (Optional) 
        """
        self.advanceChecked = advanceChecked

    def setCreatedTime(self, createdTime):
        """
        :param createdTime: (Optional) 
        """
        self.createdTime = createdTime

    def setDefaultSource(self, defaultSource):
        """
        :param defaultSource: (Optional) 
        """
        self.defaultSource = defaultSource

    def setDnsOption(self, dnsOption):
        """
        :param dnsOption: (Optional) 
        """
        self.dnsOption = dnsOption

    def setEnabled(self, enabled):
        """
        :param enabled: (Optional) 
        """
        self.enabled = enabled

    def setFtpOption(self, ftpOption):
        """
        :param ftpOption: (Optional) 
        """
        self.ftpOption = ftpOption

    def setHawkeyeId(self, hawkeyeId):
        """
        :param hawkeyeId: (Optional) 
        """
        self.hawkeyeId = hawkeyeId

    def setHttpOption(self, httpOption):
        """
        :param httpOption: (Optional) 
        """
        self.httpOption = httpOption

    def setId(self, id):
        """
        :param id: (Optional) 
        """
        self.id = id

    def setIsDeleted(self, isDeleted):
        """
        :param isDeleted: (Optional) 
        """
        self.isDeleted = isDeleted

    def setPin(self, pin):
        """
        :param pin: (Optional) 
        """
        self.pin = pin

    def setPingOption(self, pingOption):
        """
        :param pingOption: (Optional) 
        """
        self.pingOption = pingOption

    def setPop3Option(self, pop3Option):
        """
        :param pop3Option: (Optional) 
        """
        self.pop3Option = pop3Option

    def setPort(self, port):
        """
        :param port: (Optional) 端口
        """
        self.port = port

    def setSmtpOption(self, smtpOption):
        """
        :param smtpOption: (Optional) 
        """
        self.smtpOption = smtpOption

    def setStats(self, stats):
        """
        :param stats: (Optional) 
        """
        self.stats = stats

    def setTcpOption(self, tcpOption):
        """
        :param tcpOption: (Optional) 
        """
        self.tcpOption = tcpOption

    def setUdpOption(self, udpOption):
        """
        :param udpOption: (Optional) 
        """
        self.udpOption = udpOption

    def setUpdatedTime(self, updatedTime):
        """
        :param updatedTime: (Optional) 
        """
        self.updatedTime = updatedTime

