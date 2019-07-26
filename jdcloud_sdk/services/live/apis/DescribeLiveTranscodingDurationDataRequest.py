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


class DescribeLiveTranscodingDurationDataRequest(JDCloudRequest):
    """
    查询转码时长数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeLiveTranscodingDurationDataRequest, self).__init__(
            '/describeLiveTranscodingDurationData', 'GET', header, version)
        self.parameters = parameters


class DescribeLiveTranscodingDurationDataParameters(object):

    def __init__(self, startTime, ):
        """
        :param startTime: 查询起始时间，UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'

        """

        self.grade = None
        self.period = None
        self.startTime = startTime
        self.endTime = None

    def setGrade(self, grade):
        """
        :param grade: (Optional) 码率档次，可以查询指定档次的转码时长，取值：
- video_h264_4k_1
- video_h264_2k_1
- video_h264_shd_1
- video_h264_hd_1
- video_h264_sd_1
- video_h265_4k_1
- video_h265_2k_1
- video_h265_shd_1
- video_h265_hd_1
- video_h265_sd_1

        """
        self.grade = grade

    def setPeriod(self, period):
        """
        :param period: (Optional) 查询周期，取值范围：“day,month,year,followTime”，分别表示1天，1月，1年，跟随时间。默认为空，表示day。当传入followTime时，表示按Endtime-StartTime的周期，只返回一个点

        """
        self.period = period

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截至时间，UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，为空时默认为当前时间

        """
        self.endTime = endTime

