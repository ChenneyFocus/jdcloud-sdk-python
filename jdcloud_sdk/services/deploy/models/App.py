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


class App(object):

    def __init__(self, appId=None, appName=None, regionId=None, platform=None, jdsfEnabled=None, desc=None, lastDeployTime=None):
        """
        :param appId: (Optional) 应用ID
        :param appName: (Optional) 应用名称
        :param regionId: (Optional) 地域
        :param platform: (Optional) 部署平台：1云主机，2原生容器
        :param jdsfEnabled: (Optional) 使用分布式服务框架：0不使用，1使用
        :param desc: (Optional) 描述
        :param lastDeployTime: (Optional) 上次部署时间
        """

        self.appId = appId
        self.appName = appName
        self.regionId = regionId
        self.platform = platform
        self.jdsfEnabled = jdsfEnabled
        self.desc = desc
        self.lastDeployTime = lastDeployTime
