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


class UserViewInput(object):

    def __init__(self, viewId=None, viewName=None, domainId=None, ipRanges=None, isDelete=None, creator=None, createTime=None, updator=None, updateTime=None):
        """
        :param viewId: (Optional) 自定义线路ID
        :param viewName: (Optional) 自定义线路名称, 最多64个字节，允许：数字、字母、下划线，-，中文
        :param domainId: (Optional) 主域名ID
        :param ipRanges: (Optional) 用户输入的IP段，IPV4支持1.1.1.1-2.2.2.2和CIDR格式，IPV6仅支持CIDR格式
        :param isDelete: (Optional) 是否删除，0:没有删除，1:已删除
        :param creator: (Optional) 创建者
        :param createTime: (Optional) 创建时间，格式Unix timestamp，时间单位：秒
        :param updator: (Optional) 更新者
        :param updateTime: (Optional) 更新时间，格式Unix timestamp，时间单位：秒
        """

        self.viewId = viewId
        self.viewName = viewName
        self.domainId = domainId
        self.ipRanges = ipRanges
        self.isDelete = isDelete
        self.creator = creator
        self.createTime = createTime
        self.updator = updator
        self.updateTime = updateTime
