# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 10:41
from flask import render_template

from . import app_goods

# 2.使用蓝图对象定义路由
@app_goods.route('/get_goods/')
def getGoods():

    return 'get goods page'


