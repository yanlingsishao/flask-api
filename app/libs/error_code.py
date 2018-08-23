#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-20 19:29
# @Author  : Jerry Wang
# @Site    : 
# @File    : error_code.py
# @Software: PyCharm

from werkzeug.exceptions import HTTPException
from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = "ok"
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = "sorry,we mad a mistake"
    error_code = 999


class ClientTypeError(APIException):
    # 400请求参数错误，401未授权，403禁止访问，404没有找到资源
    # 500服务器未知错误
    # 200查询成功 201 创建成功  204 删除成功
    # 301 302 重定向
    code = 400
    msg = "client is invalid"
    error_code = 1006
    description = (
    )


class ParameterException(APIException):
    code = 400
    msg = "invalid parameter"
    error_code = 1000