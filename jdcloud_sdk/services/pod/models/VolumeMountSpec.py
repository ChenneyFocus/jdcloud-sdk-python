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


class VolumeMountSpec(object):

    def __init__(self, name, mountPath, readOnly=None):
        """
        :param name:  要挂载的云盘，必须使用pod volumeSpec.name。
        :param mountPath:  容器内挂载点，绝对路径，不得重复和嵌套挂载，不得挂载到根目录("/")。长度范围：[1-1024]
        :param readOnly: (Optional) 是否以只读方式挂载。默认 读写模式
        """

        self.name = name
        self.mountPath = mountPath
        self.readOnly = readOnly
