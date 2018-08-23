#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-21 17:37
# @Author  : Jerry Wang
# @Site    : 
# @File    : base.py
# @Software: PyCharm
from wtforms import Form
from app.libs.error_code import ParameterException
from flask import request


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm,self).__init__(data=data)


    def validate_for_api(self):
        valid = super(BaseForm,self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self