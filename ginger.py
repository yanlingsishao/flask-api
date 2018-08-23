#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15 15:50
# @Author  : Jerry Wang
# @Site    : 
# @File    : ginger.py
# @Software: PyCharm
from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError
from werkzeug.exceptions import HTTPException

app = create_app()

## 未知异常 aop思想
# APIException
# HTTPException
# Exception


@app.errorhandler(Exception)
def framework_error(e):
    # flask 1.0 可以捕捉所有异常
    if isinstance(e,APIException):
        return e
    if isinstance(e,HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg,code,error_code)
    else:
        if not app.config["DEBUG"]:
            return ServerError()
        else:
            raise e

if __name__ == '__main__':
    app.run(debug=True)