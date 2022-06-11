# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 12:53
# @Author  : Jaywatson
# @File    : helloworld.py
# @Soft    : backend_flaskb
import random
from os import abort

from flask_socketio import send

from libs import socketio
from libs.Response.body import ResMsg
from libs.jwt.auth_wrap import login_auth
from models.test import *
from libs.sql_factory import BaseSql
from app.test import testBp
from app.test.celery import add
from libs.exception.exception_method import ExceptionMethod
from libs.Response.code import ResponseCode


@testBp.route("/helloworld", methods=["GET"])
# @login_auth
def get():
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
    # raise ExceptionMethod('this is a test',status_code=ResponseCode.BROKENTOKEN)
    result = add.delay(1, 2)
    test_dict = dict(result=result.get(timeout=1))
    res = ResMsg(200, test_dict)
    return res.data()

def hello():
    print("----test-----")

# @socketio.on('message')
# def handle_message(data):
#     print('received message: ' + data)

@socketio.on('test  ', namespace='/test_conn')
def handle_message(message):
    socketio.emit('my response', {'data': 'Connected'}, namespace='/test_conn')
    while True:
        socketio.sleep(5)
        t = random.randint(1, 100)
        socketio.emit('server_response',
                      {'data': t}, namespace='/test_conn')