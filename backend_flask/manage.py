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
        sql = BaseSql(Test)
        data = sql._select({})
        data = sql._execute_sql('select a,c from t_test', [{'logic':'and','sql':'a in :test','key':'test','value':[1,2]}])
        res = ResMsg(200, data)
        return res.data()

api.add_resource(HelloWorld, '/')