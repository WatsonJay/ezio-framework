# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 11:37
# @Author  : Jaywatson
# @File    : SQLFactory.py
# @Soft    : backend_flask
import logging
from libs.Core import db

logger = logging.getLogger("libs")

class BaseSql:

    __model__ = None

    def __init__(self, object = None):
        self.__model__ = object

    def _insert(self, args):
        for data in args:
            model = self.__model__()
            for k, v in data.items():
                setattr(model, k, v)
            db.session.add(model)
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            return False

    def _delete(self,args):
        print(1)

    def _updata(self,args):
        print(2)

    def _select(self,args):
        print(3)