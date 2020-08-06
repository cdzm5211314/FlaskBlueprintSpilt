# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/31 16:13

from flask import Blueprint

app02 = Blueprint("app02", __name__)

@app02.route("/index/")
def app02_index():

    return "app02 index success ..."

