#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15 19:07
# @Author  : Jerry Wang
# @Site    : 
# @File    : enums.py
# @Software: PyCharm

from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201