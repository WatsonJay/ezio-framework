# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 12:53
# @Author  : Jaywatson
# @File    : __init__.py.py
# @Soft    : backend_flask
from flask import Blueprint

testBp = Blueprint("test", __name__, url_prefix="/v1/test/")

from  app.test import helloworld