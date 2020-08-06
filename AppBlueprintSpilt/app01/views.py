# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/31 15:10

from flask import Blueprint

# 创建蓝图对象,进行项目拆分
app01 = Blueprint("app01", __name__)

@app01.route('/index/')
def app01_index():

    return "app01 index success ..."