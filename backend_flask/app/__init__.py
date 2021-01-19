# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 22:27
# @Author  : Jaywatson
# @File    : __init__.py.py
# @Soft    : backend_flask

from celery import  Celery

celery_app = Celery(__name__)