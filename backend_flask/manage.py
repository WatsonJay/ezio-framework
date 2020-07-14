# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 18:33
# @Author  : Jaywatson
# @File    : manage.py
# @Soft    : backend_flask
from libs import create_app
from app.test import testBp

app = create_app()

app.register_blueprint(testBp)

