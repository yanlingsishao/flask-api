#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-8-15 15:56
# @Author  : Jerry Wang
# @Site    : 
# @File    : app.py
# @Software: PyCharm
from flask import Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(),url_prefix="/v1")


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.secure")
    app.config.from_object("app.config.setting")
    register_blueprints(app)
    register_plugin(app)
    return app
