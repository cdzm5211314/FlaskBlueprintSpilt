# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 12:26

from flask import Blueprint

# 懒加载方式
# def init_route(app):
#
#     @app.route("/")
#     def index():
#
#         return "Hello Flask"

# 创建蓝图对象
# 第一个参数表示蓝图的名字,第二个参数表示当前模块
# 注: 实际开发中,蓝图对象与蓝图名字一般保持一致
# oneobj = Blueprint("onebluename", __name__)


# 使用蓝图对象定义路由
# @oneobj.route("/index/")
# def one_index():
#
#     return "one index"


