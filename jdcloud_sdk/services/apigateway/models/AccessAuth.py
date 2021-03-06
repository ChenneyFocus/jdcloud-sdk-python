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


class AccessAuth(object):

    def __init__(self, accessAuthId=None, authUserType=None, accessKey=None, description=None, bindGroups=None, appId=None):
        """
        :param accessAuthId: (Optional) 访问授权ID
        :param authUserType: (Optional) 授权用户类型
        :param accessKey: (Optional) Access Key
        :param description: (Optional) 描述
        :param bindGroups: (Optional) 绑定分组,用英文逗号分隔
        :param appId: (Optional) api调用者的appid
        """

        self.accessAuthId = accessAuthId
        self.authUserType = authUserType
        self.accessKey = accessKey
        self.description = description
        self.bindGroups = bindGroups
        self.appId = appId
