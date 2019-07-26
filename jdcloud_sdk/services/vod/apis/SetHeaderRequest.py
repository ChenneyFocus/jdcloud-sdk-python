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


class SetHeaderRequest(JDCloudRequest):
    """
    设置域名访问头参数
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetHeaderRequest, self).__init__(
            '/domains/{domainId}:setHeader', 'POST', header, version)
        self.parameters = parameters


class SetHeaderParameters(object):

    def __init__(self, domainId, headerName, headerValue, headerType):
        """
        :param domainId: 域名ID
        :param headerName: 头参数名。当前支持的访问头参数取值范围：
  Content-Disposition
  Content-Language
  Expires
  Access-Control-Allow-Origin
  Access-Control-Allow-Methods
  Access-Control-Max-Age
  Access-Control-Expose-Headers

        :param headerValue: 头参数值
        :param headerType: 头参数类型，取值范围：req、resp
        """

        self.domainId = domainId
        self.headerName = headerName
        self.headerValue = headerValue
        self.headerType = headerType

