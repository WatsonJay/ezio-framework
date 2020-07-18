# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 18:33
# @Author  : Jaywatson
# @File    : manage.py
# @Soft    : backend_flask
from libs import create_app

app = create_app()
app.app_context().push()
