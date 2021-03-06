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


class DescribeTemplatesResponseEnd(object):

    def __init__(self, numberPages=None, numberRecords=None, pageNumber=None, pageSize=None, templateCount=None, templateList=None):
        """
        :param numberPages: (Optional) 总页数
        :param numberRecords: (Optional) 总记录数
        :param pageNumber: (Optional) 当前页码
        :param pageSize: (Optional) 分页大小
        :param templateCount: (Optional) 当查询用户自定义模板时，表示该用户目前已有的自定义模板总数量;当查询默认模板时，表示该用户目前已有的默认模板总数量
        :param templateList: (Optional) 模板列表
        """

        self.numberPages = numberPages
        self.numberRecords = numberRecords
        self.pageNumber = pageNumber
        self.pageSize = pageSize
        self.templateCount = templateCount
        self.templateList = templateList
