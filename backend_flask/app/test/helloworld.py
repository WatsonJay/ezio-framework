# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 12:53
# @Author  : Jaywatson
# @File    : helloworld.py
# @Soft    : backend_flaskb
from libs.Response.body import ResMsg
from models.test import *
from libs.sql_factory import BaseSql
from app.test import testBp

@testBp.route("/helloworld", methods=["GET"])
def get():
    test_dict = dict(name='', age=18)
    sql = BaseSql(Test)
    sql._updata(1, {'a':1,'b':1,'c':2})
    sql._delete(4)
    data = sql._select({})
    res = ResMsg(200, data)
    return res.data()