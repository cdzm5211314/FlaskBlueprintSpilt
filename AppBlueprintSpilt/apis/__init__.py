# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/8/3 10:30

from flask_restful import Api

from apis.module01_api import Module01Resource
from apis.module02_api import Module02Resource

api = Api()

def init_api(app):
    api.init_app(app)

api.add_resource(Module01Resource, '/module01/')
api.add_resource(Module02Resource, '/module02/')


