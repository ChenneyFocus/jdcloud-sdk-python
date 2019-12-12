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


class SignRequest(JDCloudRequest):
    """
    使用非对称密钥的私钥签名,签名算法仅支持RSA_PKCS1_PADDING填充方式,最大签名数据长度为4K字节
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SignRequest, self).__init__(
            '/key/{keyId}:Sign', 'POST', header, version)
        self.parameters = parameters


class SignParameters(object):

    def __init__(self, keyId, ):
        """
        :param keyId: 密钥ID
        """

        self.keyId = keyId
        self.plaintext = None

    def setPlaintext(self, plaintext):
        """
        :param plaintext: (Optional) 需要签名的数据 Base64-encoded binary data object
        """
        self.plaintext = plaintext

