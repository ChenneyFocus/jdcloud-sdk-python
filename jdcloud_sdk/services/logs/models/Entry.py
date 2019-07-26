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


class Entry(object):

    def __init__(self, content, stream=None, tags=None, timestamp=None):
        """
        :param content:  日志原文
        :param stream: (Optional) 日志流标识符,不传则使用全局日志流标识符
        :param tags: (Optional) 标签，不传则取全局标签 map[string]string
        :param timestamp: (Optional) 时间戳，UTC格式，最多支持到纳秒级别，不传入则取全局时间戳。如 2019-04-08T03:08:04.437670934Z、2019-04-08T03:08:04Z、2019-04-08T03:08:04.123Z
        """

        self.content = content
        self.stream = stream
        self.tags = tags
        self.timestamp = timestamp
