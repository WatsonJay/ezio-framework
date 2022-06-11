# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 22:17
# @Author  : Jaywatson
# @File    : handler.py
# @Soft    : backend_flask
from flask import Blueprint
from flask import request
from libs.Response.body import ResMsg
from libs.core import RedisMethod
from libs.jwt.util import generate_auth_token

jwtAuth = Blueprint('jwtAuth',__name__, url_prefix="/v1/jwt/")

@jwtAuth.route("/get-token", methods=["GET"])
def get():
    url = request.args.get('path')
    data = request.args.get('param')
    authInfo = dict(path=url, data= data)
    jwtToken = generate_auth_token(authInfo)
    RedisMethod.write(url, jwtToken, 120)
    res = ResMsg(200)
    return res.data()

