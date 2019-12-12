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


class SiteMonitorTcpOption(object):

    def __init__(self, reqContent=None, reqContentType=None, resCheck=None, resCheckType=None, timeout=None):
        """
        :param reqContent: (Optional) 请求内容
        :param reqContentType: (Optional) 请求内容类型，可选值text（文本）、hex（十六进制）
        :param resCheck: (Optional) 返回校验内容
        :param resCheckType: (Optional) 返回内容类型，可选值text（文本）、hex（十六进制）
        :param timeout: (Optional) 
        """

        self.reqContent = reqContent
        self.reqContentType = reqContentType
        self.resCheck = resCheck
        self.resCheckType = resCheckType
        self.timeout = timeout
