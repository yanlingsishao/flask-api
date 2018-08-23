#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15 16:10
# @Author  : Jerry Wang
# @Site    : 
# @File    : user.py
# @Software: PyCharm
from flask import Blueprint

from app.libs.redprint import Redprint


api = Redprint("user")


@api.route("",methods=["GET",])
def get_user():
    return 'i am wang'


@api.route("",methods=["POST",])
def create_user():
    """
    # name
    # password
    # 第三方 自己的产品 APP 小程序 用户
    # 客户端 client
    # 注册形式：短信，邮件，qq，微信....
    :return:
    """
    return 'i am qiyue,zheshipost'


