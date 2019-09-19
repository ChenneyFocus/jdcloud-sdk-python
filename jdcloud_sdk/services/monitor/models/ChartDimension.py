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


class ChartDimension(object):

    def __init__(self, dimension=None, dimensionName=None, tags=None):
        """
        :param dimension: (Optional) 分组groupCode
        :param dimensionName: (Optional) 分组名称
        :param tags: (Optional) 分组下metric对应的tags
        """

        self.dimension = dimension
        self.dimensionName = dimensionName
        self.tags = tags
