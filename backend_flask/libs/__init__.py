# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 23:53
# @Author  : Jaywatson
# @File    : __init__.py
# @Soft    : backend_flask
import os
import logging
import logging.config
from flask import Flask
from libs import get_yaml
from libs.exception import exception_handler
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
        app.config['LANG'] = profileConfig['LANG']

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

        # 注册数据库连接
        db.app = app
        db.init_app(app)

        # 注册定时任务
        if profileConfig['Scheduler']['ENABLE']:
            app.config['SCHEDULER_API_ENABLED'] = True
            app.config['SCHEDULER_JOBSTORES'] = {'default': SQLAlchemyJobStore(url=database_url)}
            app.config['SCHEDULER_EXECUTORS'] = {
                'default': {'type': 'threadpool', 'max_workers': profileConfig['Scheduler']['THREADPOOL']}}
            app.config['SCHEDULER_JOB_DEFAULTS'] = {'coalesce': False,
                                                    'max_instances': profileConfig['Scheduler']['MAX_INSTANCES']}
            scheduler_init(app)

        # 加载日志配置
        if not os.path.exists("./logs"):
            os.makedirs("./logs")
        loggingConfig = get_yaml.read_yaml_file("config/logging.yaml")
        loggingConfig['handlers']['file']['filename'] = './logs/message.log'
        logging.config.dictConfig(loggingConfig)

        # 注册蓝图
        from api.router import router
        router.append(exception_handler.exception)
        register_api(app, router)

        return app

    except Exception as e:
        print(e)
        os._exit(1)
