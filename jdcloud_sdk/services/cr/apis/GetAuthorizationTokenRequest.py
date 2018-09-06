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


class GetAuthorizationTokenRequest(JDCloudRequest):
    """
    <p>申请12小时有效期的令牌。 使用<code>docker</code> CLI push和pull镜像。</p>
<p><code>authorizationToken</code>为每个registry返回一个base64编码的字符串，解码后<code>docker login</code>命令
可完成指定registry的鉴权。JCR CLI提供<code>jcr get-login</code>进行认证处理。</p>

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetAuthorizationTokenRequest, self).__init__(
            '/regions/{regionId}/registries/{registryName}:getAuthorizationToken', 'POST', header, version)
        self.parameters = parameters


class GetAuthorizationTokenParameters(object):

    def __init__(self, regionId, registryName, ):
        """
        :param regionId: 地域 ID
        :param registryName: 注册表名称
        """

        self.regionId = regionId
        self.registryName = registryName
        self.expiredAfterHours = None

    def setExpiredAfterHours(self, expiredAfterHours):
        """
        :param expiredAfterHours: (Optional) issue新token的过期时间, 可选参数为新生成令牌的过期时间，最大值为24小时，最小值为1小时，为空则默认为12小时过期时间。

        """
        self.expiredAfterHours = expiredAfterHours
