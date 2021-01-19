# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 23:53
# @Author  : Jaywatson
# @File    : __init__.py
# @Soft    : backend_flask
import os
import logging
import logging.config
from flask import Flask
from app import celery_app
from libs import get_yaml
from libs.exception.exception_handler import exception
from libs.jwt.auth_handler import jwtAuth
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from libs.core import getDataSource, db, register_api, scheduler_init


def create_app():
    try:
        app = Flask(__name__)

        # 加载配置文件
        config = None
        langConfig = get_yaml.read_yaml_file("config/msg.yaml")
        commonConfig = get_yaml.read_yaml_file("config/application.yaml")
        profileName = commonConfig['application']['active']['profile']
        profileConfig = get_yaml.read_yaml_file("config/application-" + profileName + ".yaml")
        config = {**langConfig}
        app.config.update(config)
        app.config['LANG'] = commonConfig['LANG']

        ##添加数据库配置文件到flask App中
        _username = profileConfig['DataSource']['USERNAME']
        _password = profileConfig['DataSource']['PASSWORD']
        _host = profileConfig['DataSource']['HOST']
        _port = profileConfig['DataSource']['PORT']
        _database = profileConfig['DataSource']['DATABASE']
        _param = profileConfig['DataSource']['PARAM']
        database_url = getDataSource(_username, _password, _host, _port, _database, _param)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        ##添加redis配置文件到flask App中
        app.config['REDIS_HOST'] = profileConfig['Redis']['HOST']
        app.config['REDIS_PORT'] = profileConfig['Redis']['PORT']
        app.config['REDIS_PASS'] = profileConfig['Redis']['PASSWORD']
        app.config['REDIS_DB'] = profileConfig['Redis']['DB']
        app.config['REDIS_EXPIRE'] = profileConfig['Redis']['EXPIRE_TIME']
        app.config['REDIS_TIMEOUT'] = profileConfig['Redis']['TIMEOUT']

        # 更新Celery配置信息
        celery_conf = "redis://{}@{}:{}/{}".format(app.config['REDIS_PASS'], app.config['REDIS_HOST'], app.config['REDIS_PORT'],
                                                app.config['REDIS_DB'])
        celery_app.conf.update({"broker_url": celery_conf, "result_backend": celery_conf})

        # 注册数据库连接
        db.app = app
        db.init_app(app)

        # 注册定时任务
        if commonConfig['Scheduler']['ENABLE']:
            app.config['SCHEDULER_API_ENABLED'] = True
            app.config['SCHEDULER_JOBSTORES'] = {'default': SQLAlchemyJobStore(url=database_url)}
            app.config['SCHEDULER_EXECUTORS'] = {
                'default': {'type': 'threadpool', 'max_workers': commonConfig['Scheduler']['THREADPOOL']}}
            app.config['SCHEDULER_JOB_DEFAULTS'] = {'coalesce': False,
                                                    'max_instances': commonConfig['Scheduler']['MAX_INSTANCES']}
            scheduler_init(app)

        # 加载日志配置
        if not os.path.exists("./logs"):
            os.makedirs("./logs")
        loggingConfig = get_yaml.read_yaml_file("config/logging.yaml")
        loggingConfig['handlers']['file']['filename'] = './logs/message.log'
        logging.config.dictConfig(loggingConfig)

        # 注册蓝图
        from api.router import router
        router.append(exception)
        if commonConfig['JWT']['Authorization']:
            router.append(jwtAuth)
        register_api(app, router)

        return app

    except Exception as e:
        print(e)
        os._exit(1)
