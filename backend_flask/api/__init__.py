# -*- coding: utf-8 -*-
# @Time    : 2020/6/18 12:37
# @Author  : Jaywatson
# @File    : __init__.py
# @Soft    : backend_flask

import os
import logging
import logging.config
from flask import Flask
from libs import GetYaml
from libs.Core import getDataSource, db

def create_app():
    try:
        app = Flask(__name__)

        #加载配置文件
        config = None
        langConfig = GetYaml.read_yaml_file("config/msg.yaml")
        commonConfig = GetYaml.read_yaml_file("config/application.yaml")
        profileName = commonConfig['application']['active']['profile']
        profileConfig = GetYaml.read_yaml_file("config/application-" + profileName + ".yaml")
        config = {**commonConfig,**profileConfig,**langConfig}
        app.config.update(config)

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

        # 注册数据库连接
        db.app = app
        db.init_app(app)

        #加载日志配置
        if not os.path.exists("./logs"):
            os.makedirs("./logs")
        loggingConfig = GetYaml.read_yaml_file("config/logging.yaml")
        loggingConfig['handlers']['file']['filename'] = './logs/message.log'
        logging.config.dictConfig(loggingConfig)

        return app
    except Exception as e:
        print(e)
        os._exit(1)
