# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/8/3 10:34

from flask_restful import Resource


class Module02Resource(Resource):

    def get(self):
        return {"msg": "module02 get success"}

    def post(self):
        return {"msg": "module02 post success"}




