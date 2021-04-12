# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 18:33
# @Author  : Jaywatson
# @File    : manage.py
# @Soft    : backend_flask
import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    # print(f"load `{env_path}` environment file")
    load_dotenv(env_path)

from libs import create_app
from app import celery_app

app = create_app(celery= celery_app)
app.app_context().push()
