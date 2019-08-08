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


class DelView(object):

    def __init__(self, domainName, viewName, viewId, ):
        """
        :param domainName:  主域名
        :param viewName:  自定义线路名称, 最多64个字节，允许：数字、字母、下划线，-，中文
        :param viewId:  自定义线路ID
        """

        self.domainName = domainName
        self.viewName = viewName
        self.viewId = viewId
