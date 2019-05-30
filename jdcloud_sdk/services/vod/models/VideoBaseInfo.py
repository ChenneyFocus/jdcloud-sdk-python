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


class VideoBaseInfo(object):

    def __init__(self, videoId=None, videoName=None, description=None, categoryId=None, categoryName=None, tags=None, duration=None, coverImgUrl=None):
        """
        :param videoId: (Optional) 视频ID
        :param videoName: (Optional) 视频名称
        :param description: (Optional) 视频描述
        :param categoryId: (Optional) 
        :param categoryName: (Optional) 分类名称
        :param tags: (Optional) 标签
        :param duration: (Optional) 视频时长
        :param coverImgUrl: (Optional) 封面地址
        """

        self.videoId = videoId
        self.videoName = videoName
        self.description = description
        self.categoryId = categoryId
        self.categoryName = categoryName
        self.tags = tags
        self.duration = duration
        self.coverImgUrl = coverImgUrl
