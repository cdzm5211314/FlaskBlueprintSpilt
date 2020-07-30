# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 10:41

from . import app_order

# 2.使用蓝图对象注册蓝图路由
@app_order.route('/get_order/')
def getOrder():
    return 'get order page'


