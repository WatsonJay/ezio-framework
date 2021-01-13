# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 12:53
# @Author  : Jaywatson
# @File    : helloworld.py
# @Soft    : backend_flaskb
from os import abort

from libs.Response.body import ResMsg
from libs.jwt.wrap import login_auth
from models.test import *
from libs.sql_factory import BaseSql
from app.test import testBp
from libs.exception.util_exception import UtilException


@testBp.route("/helloworld", methods=["GET"])
@login_auth
def get():
    test_dict = dict(name='', age=18)
    # sql = BaseSql(Test)
    # sql._updata(1, {'a':1,'b':1,'c':2})
    # sql._delete(4)
    # data = sql._select({})
    # res = ResMsg(200, test_dict)
    # test = {'trigger':'interval','interval':{'seconds':5}}
    # from libs.task_scheduler import TaskScheduler
    # TaskScheduler.add_job('test','app.test.helloworld:hello',None,**test)
    #TaskScheduler.remove_job('test')
    # return res.data()
    raise UtilException('this is a test',status_code=1010)

def hello():
    print("----test-----")