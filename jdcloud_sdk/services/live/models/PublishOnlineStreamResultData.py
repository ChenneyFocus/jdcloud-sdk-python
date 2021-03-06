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


class PublishOnlineStreamResultData(object):

    def __init__(self, appName=None, streamName=None, clientIp=None, serverIp=None, frameRate=None, frameLossRate=None, lastActive=None, realFps=None, uploadSpeed=None, videoCodec=None, videoDataRate=None, audioCodec=None):
        """
        :param appName: (Optional) APP名称

        :param streamName: (Optional) 流名称

        :param clientIp: (Optional) 客户端ip

        :param serverIp: (Optional) 边缘节点ip

        :param frameRate: (Optional) 帧率

        :param frameLossRate: (Optional) 丢帧率

        :param lastActive: (Optional) 最近活跃时间

        :param realFps: (Optional) 实时帧率

        :param uploadSpeed: (Optional) 上传速度  单位：KB/s

        :param videoCodec: (Optional) 视频codec，取值：
- VideoAVC = 7
- VideoHEVC = 12

        :param videoDataRate: (Optional) 视频码率 单位：KB/s

        :param audioCodec: (Optional) 音频codec，取值：
- AudioReserved1 = 16
- AudioDisabled = 17
- AudioLinearPCMPlatformEndian = 0
- AudioADPCM = 1
- AudioMP3 = 2
- AudioLinearPCMLittleEndian = 3
- AudioNellymoser16kHzMono = 4
- AudioNellymoser8kHzMono = 5
- AudioNellymoser = 6
- AudioReservedG711AlawLogarithmicPCM = 7
- AudioReservedG711MuLawLogarithmicPCM = 8
- AudioReserved = 9
- AudioAAC = 10
- AudioSpeex = 11
- AudioReservedMP3_8kHz = 14
- AudioReservedDeviceSpecificSound = 15

        """

        self.appName = appName
        self.streamName = streamName
        self.clientIp = clientIp
        self.serverIp = serverIp
        self.frameRate = frameRate
        self.frameLossRate = frameLossRate
        self.lastActive = lastActive
        self.realFps = realFps
        self.uploadSpeed = uploadSpeed
        self.videoCodec = videoCodec
        self.videoDataRate = videoDataRate
        self.audioCodec = audioCodec
