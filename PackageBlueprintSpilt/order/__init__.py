# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 10:41

from flask import Blueprint

# 1.创建一个蓝图的对象,蓝图对象就是一个小模块的抽象概念
# Blueprint必须指定两个参数,第一个参数表示蓝图的名称，__name__表示蓝图所在模块
app_order = Blueprint('order', __name__, static_folder='static', template_folder='templates')

# 在__init__.py文件中,把视图函数加载进来,让蓝图与应用程序知道有视图函数的存在
# from .views import getOrder


