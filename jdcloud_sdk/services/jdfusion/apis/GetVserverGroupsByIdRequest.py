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


class GetVserverGroupsByIdRequest(JDCloudRequest):
    """
    根据过滤条件，取得服务器组的信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetVserverGroupsByIdRequest, self).__init__(
            '/regions/{regionId}/vpc_vserverGroups/{id}', 'GET', header, version)
        self.parameters = parameters


class GetVserverGroupsByIdParameters(object):

    def __init__(self, regionId, id, ):
        """
        :param regionId: 地域ID
        :param id: 服务器组ID
        """

        self.regionId = regionId
        self.id = id

