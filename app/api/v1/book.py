#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15 16:10
# @Author  : Jerry Wang
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from flask import Blueprint
from app.libs.redprint import Redprint

api = Redprint("book")


@api.route("",methods=["GET",])
def get_book():
    return 'i am book'
