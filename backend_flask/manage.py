# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 18:33
# @Author  : Jaywatson
# @File    : manage.py
# @Soft    : backend_flask
from flask_restful import Api, Resource
from api import create_app
from libs.Response.Body import ResMsg
from models.test import *
from libs.SQLFactory import BaseSql

app = create_app()
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        test_dict = dict(name='', age=18)
        res = ResMsg(200,test_dict)
        sql = BaseSql(Test)
        sql._insert([{"a":"1","b":"2","c":"3"}])
        return res.data()

api.add_resource(HelloWorld, '/')