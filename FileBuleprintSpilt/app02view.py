# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 13:02

from flask import Blueprint


# 1.创建蓝图对象
# 第一个参数表示蓝图的名字,第二个参数表示当前模块
# 注: 实际开发中,蓝图对象与蓝图名字一般保持一致
app02 = Blueprint('app02', __name__)

# 2.使用蓝图对象注册蓝图路由
@app02.route('/app02index/')
def app02_index():

    return 'app02 index ...'



