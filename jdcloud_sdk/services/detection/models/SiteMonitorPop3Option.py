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


class SiteMonitorPop3Option(object):

    def __init__(self, passwd, protocol, user, timeout=None):
        """
        :param passwd:  
        :param protocol:  协议类型，可选值：pop3、pop3s
        :param timeout: (Optional) 
        :param user:  
        """

        self.passwd = passwd
        self.protocol = protocol
        self.timeout = timeout
        self.user = user
