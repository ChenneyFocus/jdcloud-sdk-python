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


class ProbeInfo(object):

    def __init__(self, name=None, privateIp=None, probeResult=None, probeStatus=None, publicIp=None, targetStatus=None, uuid=None, vmStatus=None):
        """
        :param name: (Optional) 探测源的所在主机名称
        :param privateIp: (Optional) 探测源的内网ip
        :param probeResult: (Optional) 探测结果,缺点返回null,对应前端显示 "--" ,1:探测正常，2：探测失败，3：探测超时
        :param probeStatus: (Optional) 插件状态，  1：正常，2：异常
        :param publicIp: (Optional) 探测源的公网ip
        :param targetStatus: (Optional) 探测目标状态，1：正常，2：异常(探测失败、探测超时)，缺点返回null,对应前端显示 "--"
        :param uuid: (Optional) 探测源主机的uuid
        :param vmStatus: (Optional) 云主机状态，对应云主机的状态,当找不到云主机，状态为"unExist"
        """

        self.name = name
        self.privateIp = privateIp
        self.probeResult = probeResult
        self.probeStatus = probeStatus
        self.publicIp = publicIp
        self.targetStatus = targetStatus
        self.uuid = uuid
        self.vmStatus = vmStatus
