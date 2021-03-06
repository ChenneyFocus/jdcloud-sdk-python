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


class TaskAddressInfo(object):

    def __init__(self, storageType=None, accessKey=None, secretKey=None, endpoint=None, bucket=None, prefix=None, cloudID=None):
        """
        :param storageType: (Optional) 任务类型:源地址中支持 s3file, aliyunfile，目标现在只支持s3file
        :param accessKey: (Optional) 源地址的accesskey
        :param secretKey: (Optional) 源地址的securitykey
        :param endpoint: (Optional) 源地址的Endpoint
        :param bucket: (Optional) 源地址的Bucket
        :param prefix: (Optional) 源地址的Prefix，不能以/开头
        :param cloudID: (Optional) 云信息ID
        """

        self.storageType = storageType
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.endpoint = endpoint
        self.bucket = bucket
        self.prefix = prefix
        self.cloudID = cloudID
