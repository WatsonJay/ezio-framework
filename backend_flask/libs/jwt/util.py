    # -*- coding: utf-8 -*-
# @Time    : 2021/1/13 17:28
# @Author  : Jaywatson
# @File    : util.py
# @Soft    : backend_flask
import os
from datetime import datetime, timedelta
import jwt

key = os.getenv('JWT_SECRET_KEY').encode('utf-8')

