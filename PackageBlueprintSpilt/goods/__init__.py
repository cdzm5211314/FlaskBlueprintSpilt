# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 10:41

from flask import Blueprint

# 1.创建一个蓝图的对象,蓝图对象就是一个小模块的抽象概念
# Blueprint必须指定两个参数,第一个参数表示蓝图的名称，__name__表示蓝图所在模块
app_goods = Blueprint('goods', __name__, static_folder='static', template_folder='templates')



