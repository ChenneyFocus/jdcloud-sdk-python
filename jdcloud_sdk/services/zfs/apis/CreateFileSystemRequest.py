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


class CreateFileSystemRequest(JDCloudRequest):
    """
    - 创建一个新的文件系统，为这个文件系统分配一个Id

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateFileSystemRequest, self).__init__(
            '/regions/{regionId}/fileSystems', 'POST', header, version)
        self.parameters = parameters


class CreateFileSystemParameters(object):

    def __init__(self, regionId, name, description, clientToken):
        """
        :param regionId: 地域ID
        :param name: 文件系统名称
        :param description: 文件系统描述
        :param clientToken: 幂等性参数(只支持数字、大小写字母，且不能超过64字符)
        """

        self.regionId = regionId
        self.name = name
        self.description = description
        self.clientToken = clientToken
