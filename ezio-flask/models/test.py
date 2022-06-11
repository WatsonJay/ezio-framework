# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 12:13
# @Author  : Jaywatson
# @File    : test.py
# @Soft    : backend_flask

from libs.core import db

# 新建用户
class Test(db.Model):
    """
    用户表
    """
    __tablename__ = 't_test'
    a = db.Column(db.String(20), primary_key=True)
    b = db.Column(db.String(20), nullable=False)  # 用户姓名
    c = db.Column(db.String(20), nullable=False)  # 用户年龄
