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


class ProductTxt(object):

    def __init__(self, id=None, productId=None, templet=None, txt=None, sort=None, createTime=None, updateTime=None, lang=None):
        """
        :param id: (Optional) 主键id
        :param productId: (Optional) 产品id
        :param templet: (Optional) 模板类型
        :param txt: (Optional) 内容(JSON字符串)
        :param sort: (Optional) 排序
        :param createTime: (Optional) 修改时间
        :param updateTime: (Optional) 修改时间
        :param lang: (Optional) 语言：中文cn；英文en
        """

        self.id = id
        self.productId = productId
        self.templet = templet
        self.txt = txt
        self.sort = sort
        self.createTime = createTime
        self.updateTime = updateTime
        self.lang = lang
