# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 23:51
# @Author  : Jaywatson
# @File    : Helloworld.py
# @Soft    : backend_flask
from flask_restful import Resource
from libs.Response.Body import ResMsg
from models.test import *
from libs.SQLFactory import BaseSql

class HelloWorld(Resource):
    def get(self):
        test_dict = dict(name='', age=18)
        sql = BaseSql(Test)
        sql._updata(1, {'a':1,'b':1,'c':2})
        sql._delete(4)
        data = sql._select({})
        res = ResMsg(200, data)
        return res.data()