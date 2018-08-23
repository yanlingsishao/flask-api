#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-20 17:47
# @Author  : Jerry Wang
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired,length,Regexp,Email
from wtforms import ValidationError


from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(),length(
        min=5,max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self,value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidata email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2,max=22)])

    def validate_account(self,value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError