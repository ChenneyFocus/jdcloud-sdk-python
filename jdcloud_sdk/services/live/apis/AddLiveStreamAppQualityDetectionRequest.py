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


class AddLiveStreamAppQualityDetectionRequest(JDCloudRequest):
    """
    添加应用质量检测配置
- 添加应用级别的质量检测模板配置

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddLiveStreamAppQualityDetectionRequest, self).__init__(
            '/qualityDetectionApps:template', 'POST', header, version)
        self.parameters = parameters


class AddLiveStreamAppQualityDetectionParameters(object):

    def __init__(self, publishDomain, appName, template):
        """
        :param publishDomain: 推流域名
        :param appName: 应用名称
        :param template: 质量检测模板

        """

        self.publishDomain = publishDomain
        self.appName = appName
        self.template = template

