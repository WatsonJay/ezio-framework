# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 12:44
# @Author  : Jaywatson
# @File    : router.py
# @Soft    : backend_flask
from app.test import testBp
from app.test.hello import get1

router = [
    testBp,
    # {get1: "/helloworld1"}
]