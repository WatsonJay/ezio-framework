    # -*- coding: utf-8 -*-
# @Time    : 2021/1/13 17:28
# @Author  : Jaywatson
# @File    : util.py
# @Soft    : backend_flask
import os
import json
import jwt
from datetime import datetime, timedelta
from libs.Response.code import ResponseCode
from libs.aes_crypt import encrypt,decrypt
from libs.exception.exception_method import ExceptionMethod

key = os.getenv('JWT_SECRET_KEY').encode('utf-8')

def generate_auth_token(dict={}, algorithm: str = 'HS256', exp: float = 2):

    """
    生成access_token
    :param user_name: 自定义部分
    :param algorithm:加密算法
    :param exp:过期时间
    :return:token
    """
    now = datetime.utcnow()
    exp_datetime = now + timedelta(hours=exp)
    access_payload = {
        'exp': exp_datetime,
        'flag': 0,  # 标识是否为一次性token，0是，1不是
        'iat': now,  # 开始时间
        'iss': dict['path'],  # 签名
        'info': encrypt(dict['data'])  # 自定义部分
    }
    access_token = jwt.encode(access_payload, key, algorithm=algorithm)
    return access_token

def decode_auth_token(token: str, issuer: str = ''):
    """
    解密token
    :param token:token字符串
    :return:
    """
    try:
        if issuer != '' :
            payload = jwt.decode(token, issuer=issuer, key=key, algorithms=["HS256"])
        else :
            payload = jwt.decode(token, key=key, algorithms=["HS256"])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.InvalidSignatureError) as e:
        raise ExceptionMethod(status_code=ResponseCode.TOKENERROR)
    else:
        return payload

def identify(auth_header: str, issuer: str = ''):
    """
    用户鉴权
    :return:
    """
    try:
        if auth_header:
            payload = decode_auth_token(auth_header,issuer)
            if not payload:
                return False
            if "info" in payload and "flag" in payload:
                temp = payload["info"]
                info = json.loads(decrypt(temp))
                return info
            else:
                return False
        else:
            return False
    except Exception as e:
        raise ExceptionMethod(status_code=ResponseCode.JWTERROR)