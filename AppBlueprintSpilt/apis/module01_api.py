# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/8/3 10:33


from flask_restful import Resource


class Module01Resource(Resource):

    def get(self):
        return {"msg": "module01 get success"}

    def post(self):
        return {"msg": "module01 post success"}



