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


class DeleteSdkSmsSignRequest(JDCloudRequest):
    """
    删除短信签名接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteSdkSmsSignRequest, self).__init__(
            '/regions/{regionId}/deleteSdkSmsSign', 'POST', header, version)
        self.parameters = parameters


class DeleteSdkSmsSignParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.signId = None

    def setSignId(self, signId):
        """
        :param signId: (Optional) signId参数
        """
        self.signId = signId
