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


class AddCustomLiveStreamTranscodeTemplateRequest(JDCloudRequest):
    """
    添加自定义转码模板
- 系统为您预设了标准转码模板,如果不能满足您的转码需求,可以通过此接口添加自定义转码模板
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
        super(AddCustomLiveStreamTranscodeTemplateRequest, self).__init__(
            '/transcodeCustoms:template', 'POST', header, version)
        self.parameters = parameters


class AddCustomLiveStreamTranscodeTemplateParameters(object):

    def __init__(self, videoCodeRate, videoFrameRate, template, audioCodec, audioFormat, audioSampleRate, audioChannel, audioCodeRate):
        """
        :param videoCodeRate: 转码输出的码率值
- 取值范围: [1,6000]
- 单位: kpbs

        :param videoFrameRate: 转码输出的帧率值
- 取值：[1,30]

        :param template: 转码模板(转码流输出后缀)
- 取值要求：数字、大小写字母或短横线("-"),必须以数字或字母作为开头和结尾,长度不超过50字符
- <b>注意: 不能与系统的标准的转码模板和当前用户已自定义命名重复</b>
- 系统标准转码模板
  ld (h.264/640*360/15f)
  sd (h.264/960*540/24f)
  hd (h.264/1280*720/25f)
  shd (h.264/1920*1080/30f)
  ld.265 (h.265/640*360/15f)
  sd.265 (h.265/960*540/24f)
  hd.265 (h.265/1280*720/25f)
  shd.265 (h.265/1920*1080/30f)

        :param audioCodec: 转码输出音频编码格式
- 取值: aac、mp3
- 不区分大小写

        :param audioFormat: 转码输出音频格式
- 取值: aac_lc，aac_low，aac_he，aac_he_v2
- 不区分大小写

        :param audioSampleRate: 转码输出音频采样率
- 取值: [44100,48000]

        :param audioChannel: 转码输出音频通道数
  1: 单声道
  2: 双声道

        :param audioCodeRate: 转码输出音频码率
- 取值: [16,128]
- 单位: kbps

        """

        self.templateName = None
        self.videoCodec = None
        self.videoCodeRate = videoCodeRate
        self.videoFrameRate = videoFrameRate
        self.width = None
        self.height = None
        self.template = template
        self.audioCodec = audioCodec
        self.audioFormat = audioFormat
        self.audioSampleRate = audioSampleRate
        self.audioChannel = audioChannel
        self.audioCodeRate = audioCodeRate

    def setTemplateName(self, templateName):
        """
        :param templateName: (Optional) 转码模板名称
- 长度范围：[1,50]

        """
        self.templateName = templateName

    def setVideoCodec(self, videoCodec):
        """
        :param videoCodec: (Optional) 视频编码格式，取值：h264,h265，默认h264

        """
        self.videoCodec = videoCodec

    def setWidth(self, width):
        """
        :param width: (Optional) 转码输出视频宽度
- 取值: [128,1920]
- 如果(width,height)只设置其中之一,则按所设置参数项等比缩放另一项输出转码
- 如果(width,height)都不设置，则按源流大小输出转码

        """
        self.width = width

    def setHeight(self, height):
        """
        :param height: (Optional) 转码输出视频宽度
- 取值: [128,1920]
- 如果(width,height)只设置其中之一,则按所设置参数项等比缩放另一项输出转码
- 如果(width,height)都不设置，则按源流大小输出转码

        """
        self.height = height

