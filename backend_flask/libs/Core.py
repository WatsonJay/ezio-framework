# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 11:00
# @Author  : Jaywatson
# @File    : core.py
# @Soft    : backend_flask
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from libs.AESCrypt import decrypt
import redis

db = SQLAlchemy()

'''数据库连接词'''
def getDataSource(USERNAME = '', PASSWORD = '', HOST = '', PORT = '', DATABASE = '', PARAM = ''):
    if PASSWORD != '' and PASSWORD.startswith('AES@'):
        PASSWORD = decrypt(PASSWORD[4:])
    database_url ='mysql+pymysql://{}:{}@{}:{}/{}?{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE,PARAM)
    return database_url

'''redis数据库操作'''
class Redis(object):

    '''获取配置'''
    @staticmethod
    def _get_config():
        host = current_app.config['REDIS_HOST']
        port = current_app.config['REDIS_PORT']
        password = current_app.config['REDIS_PASS']
        db = current_app.config['REDIS_DB']
        redis_config = redis.StrictRedis(host, port, db, password)
        return redis_config

    '''写入键值对'''
    @classmethod
    def write(cls, key, value, expire=None):
        redis_config = cls._get_config()
        if expire:
            expire_in_seconds = expire
            redis_config.set(key, value, ex=expire_in_seconds)
        else:
            redis_config.set(key, value)

    '''读取键值对'''
    @classmethod
    def read(cls, key):
        redis_config = cls._get_config()
        value = redis_config.get(key)
        return value.decode('utf-8') if value else ''

    '''写入hash表'''
    @classmethod
    def hset(cls, name, key, value):
        redis_config = cls._get_config()
        redis_config.hset(name, key, value)

    '''读取指定hash表的所有给定字段的值'''
    @classmethod
    def hmset(cls, key, *value):
        redis_config = cls._get_config()
        value = redis_config.hmset(key, *value)
        return value

    '''读取指定hash表的键值'''
    @classmethod
    def hget(cls, name, key):
        redis_config = cls._get_config()
        value = redis_config.hget(name, key)
        return value.decode('utf-8') if value else value

    '''获取指定hash表所有的值'''
    @classmethod
    def hgetall(cls, name):
        redis_config = cls._get_config()
        return redis_config.hgetall(name)

    '''删除一个或者多个'''
    @classmethod
    def delete(cls, *names):
        redis_config = cls._get_config()
        redis_config.delete(*names)

    '''删除指定hash表的键值'''
    @classmethod
    def hdel(cls, name, key):
        redis_config = cls._get_config()
        redis_config.hdel(name, key)

    '''设置过期时间'''
    @classmethod
    def expire(cls, name, expire=None):
        if expire:
            expire_in_seconds = expire
            redis_config = cls._get_config()
            redis_config.expire(name, expire_in_seconds)
