#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-21 18:59
# @Author  : Jerry Wang
# @Site    : 
# @File    : token.py
# @Software: PyCharm
from app.libs.redprint import Redprint
from app.libs.enums import ClientTypeEnum
from app.validators.forms import ClientForm

api = Redprint("token")


@api.route('',methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL:User.verify,
    }
