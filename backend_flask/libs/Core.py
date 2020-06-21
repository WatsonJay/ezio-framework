# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 11:00
# @Author  : Jaywatson
# @File    : core.py
# @Soft    : backend_flask
from flask_sqlalchemy import SQLAlchemy
from libs.AESCrypt import decrypt

db = SQLAlchemy()

def getDataSource(USERNAME = '', PASSWORD = '', HOST = '', PORT = '', DATABASE = '', PARAM = ''):
    if PASSWORD != '' and PASSWORD.startswith('AES@'):
        PASSWORD = decrypt(PASSWORD[4:])
    database_url ='mysql+pymysql://{}:{}@{}:{}/{}?{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE,PARAM)
    return database_url