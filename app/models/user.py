#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-20 18:08
# @Author  : Jerry Wang
# @Site    : 
# @File    : user.py
# @Software: PyCharm
from app.models.base import Base,db
from sqlalchemy import Column,Integer,String,SmallInteger
from werkzeug.security import generate_password_hash


class User(Base):
    id = Column(Integer,primary_key=True)
    email = Column(String(24),unique=True,nullable=False)
    nickname = Column(String(24))
    _password = Column('password',String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname,account,secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

