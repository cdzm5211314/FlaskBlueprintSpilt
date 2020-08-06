# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/31 15:10

from AppBlueprintSpilt.extends import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
