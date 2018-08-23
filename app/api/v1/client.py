#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15 19:05
# @Author  : Jerry Wang
# @Site    : 
# @File    : client.py
# @Software: PyCharm
from flask import request
from app.libs.redprint import Redprint
from app.validators.forms import ClientTypeEnum

from app.validators.forms import ClientForm
from app.models.user import User
from app.validators.forms import UserEmailForm
from app.libs.error_code import ClientTypeError,Success
api = Redprint("client")


@api.route("/register",methods=['POST'])
def create_client():

    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL:__register_user_by_email,
        }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    print(form.nickname.data)
    User.register_by_email(form.nickname.data,
                           form.account.data,form.secret.data)
