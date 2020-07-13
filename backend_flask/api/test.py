# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 23:38
# @Author  : Jaywatson
# @File    : test.py
# @Soft    : backend_flask
from app.test.Helloworld import *
from manage import ApiCenter

ApiCenter.add_resource(HelloWorld, '/')