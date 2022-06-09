# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 18:54
# @Author  : Jaywatson
# @File    : wrapper.py
# @Soft    : backend_flask

from functools import wraps

from libs.exception.exception_method import ExceptionMethod
from libs.jwt.util import identify
from flask import request
from libs.core import RedisMethod
from libs.Response.code import ResponseCode

def login_auth(f):
    """
    登陆保护，验证用户是否登陆
    :param f:
    :return:
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization", default=None)
        path = request.path
        method = request.method
        if token == RedisMethod.read(path) or token == '':
            raise ExceptionMethod('this is a test', status_code=ResponseCode.INVALIDTOKEN)
        infoDict = identify(token)
        if method == 'GET':
            data = request.args
        elif method == 'POST':
            data = request.json
        else:
            data = {}
        if data != infoDict:
            raise ExceptionMethod('this is a test', status_code=ResponseCode.INVALIDTOKEN)
        RedisMethod.delete(path)
        return f(*args, **kwargs)
    return wrapper
