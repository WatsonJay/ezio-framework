    # -*- coding: utf-8 -*-
# @Time    : 2021/1/13 17:28
# @Author  : Jaywatson
# @File    : util.py
# @Soft    : backend_flask
import os
import json
from datetime import datetime, timedelta
from libs.aes_crypt import encrypt,decrypt
import jwt

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
    authInfo = json.dumps(dict)
    access_payload = {
        'exp': exp_datetime,
        'flag': 0,  # 标识是否为一次性token，0是，1不是
        'iat': now,  # 开始时间
        'iss': 'qin',  # 签名
        'info': encrypt(authInfo)  # 自定义部分
    }
    access_token = jwt.encode(access_payload, key, algorithm=algorithm)
    return access_token

def decode_auth_token(token: str):
    """
    解密token
    :param token:token字符串
    :return:
    """
    try:
        # 取消过期时间验证
        # payload = jwt.decode(token, key, options={'verify_exp': False})
        payload = jwt.decode(token, key=key, )
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.InvalidSignatureError):
        return ""
    else:
        return payload

def identify(auth_header: str):
    """
    用户鉴权
    :return:
    """
    if auth_header:
        payload = decode_auth_token(auth_header)
        if not payload:
            return False
        if "info" in payload and "flag" in payload:
            temp = payload["info"]
            info = json.load(decrypt(temp))
            return info
        else:
            return False
    else:
        return False