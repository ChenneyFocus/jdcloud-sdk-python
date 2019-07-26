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


class AddTemplateRequest(JDCloudRequest):
    """
    增加富媒体短信内容接口
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(AddTemplateRequest, self).__init__(
            '/regions/{regionId}/addTemplate', 'POST', header, version)
        self.parameters = parameters


class AddTemplateParameters(object):

    def __init__(self, regionId, appId, signType, purpose, signCardType, aptitudes, title, description, unsubscribe, content):
        """
        :param regionId: Region ID
        :param appId: 应用ID
        :param signType: 签名类型 0:公司 1:app 2:网站 3:公众号 4:商标 5:政府机关
        :param purpose: 用途 0:自用 1:他用
        :param signCardType: 资质证明类型 0:三证合一 1:企业营业执照 2:组织机构代码证书 3:社会信用代码证书
        :param aptitudes: 资质证明图片必须是jpg图片的base64编码，只支持jpg图片
        :param title: 多媒体内容的标题
        :param description: 多媒体内容的描述
        :param unsubscribe: 是否支持退订 0:不支持退订 1:支持退订
        :param content: 短信内容
        """

        self.regionId = regionId
        self.appId = appId
        self.signType = signType
        self.purpose = purpose
        self.signCardType = signCardType
        self.aptitudes = aptitudes
        self.title = title
        self.description = description
        self.unsubscribe = unsubscribe
        self.content = content

