# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 18:33
# @Author  : Jaywatson
# @File    : manage.py
# @Soft    : backend_flask
from libs import create_app
from flask_restful import Api
app = create_app()
ApiCenter = Api(app)

import api