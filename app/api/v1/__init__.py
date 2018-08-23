#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15 16:10
# @Author  : Jerry Wang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint
from app.api.v1 import user,book,client


def create_blueprint_v1():
    bp_v1 = Blueprint("v1",__name__)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1