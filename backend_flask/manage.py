# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 18:33
# @Author  : Jaywatson
# @File    : manage.py
# @Soft    : backend_flask
from flask_restful import Api, Resource
from api import create_app
from libs.Response.Body import ResMsg

app = create_app()
api = Api(app)

class HelloWorld(Resource):

    def get(self):

        test_dict = dict(name='', age=18)
        res = ResMsg(200,test_dict)
        return res.data()

api.add_resource(HelloWorld, '/')