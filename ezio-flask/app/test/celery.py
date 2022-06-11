# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 16:35
# @Author  : Jaywatson
# @File    : celery.py
# @Soft    : backend_flask
from app import celery_app

@celery_app.task
def add(x, y):
    """
    加法
    :param x:
    :param y:
    :return:
    """
    return str(x + y)
