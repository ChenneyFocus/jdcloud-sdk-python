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


class DescribeCustomLiveStreamTranscodeTemplateRequest(JDCloudRequest):
    """
    查询用户自定义转码模板详情
- 查询用户自定义转码模板详情
- 系统标准转码模板
      ld (h.264/640*360/15f)
      sd (h.264/960*540/24f)
      hd (h.264/1280*720/25f)
      shd (h.264/1920*1080/30f)
      ld.265 (h.265/640*360/15f)
      sd.265 (h.265/960*540/24f)
      hd.265 (h.265/1280*720/25f)
      shd.265 (h.265/1920*1080/30f)

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeCustomLiveStreamTranscodeTemplateRequest, self).__init__(
            '/transcodeCustoms/{template}', 'GET', header, version)
        self.parameters = parameters


class DescribeCustomLiveStreamTranscodeTemplateParameters(object):

    def __init__(self, template, ):
        """
        :param template: 转码模板
        """

        self.template = template

