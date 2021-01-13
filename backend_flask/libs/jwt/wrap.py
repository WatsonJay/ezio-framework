# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 18:54
# @Author  : Jaywatson
# @File    : wrapper.py
# @Soft    : backend_flask

from functools import wraps

from flask import request


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
        
        return f(*args, **kwargs)
    return wrapper
