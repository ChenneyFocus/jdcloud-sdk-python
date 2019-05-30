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


class CategoryTreeNode(object):

    def __init__(self, id=None, name=None, level=None, description=None, children=None, createTime=None, updateTime=None):
        """
        :param id: (Optional) 分类ID
        :param name: (Optional) 分类名称
        :param level: (Optional) 分类级别
        :param description: (Optional) 分类描述信息
        :param children: (Optional) 
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        """

        self.id = id
        self.name = name
        self.level = level
        self.description = description
        self.children = children
        self.createTime = createTime
        self.updateTime = updateTime
