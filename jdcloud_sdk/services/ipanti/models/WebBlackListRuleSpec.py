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


class WebBlackListRuleSpec(object):

    def __init__(self, name, mode, value, action, status, key=None, pattern=None, actionValue=None):
        """
        :param name:  黑名单规则名称
        :param mode:  模式:<br>- 0: uri<br>- 1: ip<br>- 2: cookie<br>- 3: geo<br>- 4: header
        :param key: (Optional) 匹配 key. mode 为 cookie 和 header 时必传.
- mode 为 cookie 时, 传 cookie 的 name
- mode 为 header 时, 传 header 的 key

        :param value:  匹配 value.
- mode 为 uri 时, 传要匹配的 uri
- mode 为 ip 时, 传引用的 ip 黑白名单 Id
- mode 为 cookie 时, 传 cookie 的 value
- mode 为 geo 时, 传 geo 区域编码以 ',' 分隔的字符串. 查询 <a href="http://docs.jdcloud.com/anti-ddos-pro/api/describegeoareas">describeGeoAreas</a> 接口获取可设置的地域编码列表
- mode 为 header 时, 传 header 的 value

        :param pattern: (Optional) 匹配规则. mode 为 uri, cookie 和 header 时必传. 支持以下匹配规则
- 0: 完全匹配
- 1: 前缀匹配
- 2: 包含
- 3: 正则匹配
- 4: 后缀匹配

        :param action:  命中后处理动作
- 0: 阻断
- 1: 跳转
- 2: 验证码

        :param actionValue: (Optional) 命中后处理值, action 为 1 时传跳转路径

        :param status:  规则状态.
- 0: 关闭
- 1: 开启

        """

        self.name = name
        self.mode = mode
        self.key = key
        self.value = value
        self.pattern = pattern
        self.action = action
        self.actionValue = actionValue
        self.status = status
