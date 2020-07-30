# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2020-05-02 10:37

from flask import Blueprint


# 1.创建蓝图对象
# 第一个参数表示蓝图的名字,第二个参数表示当前模块
# 注: 实际开发中,蓝图对象与蓝图名字一般保持一致
app01 = Blueprint('app01', __name__)

# 2.使用蓝图对象注册蓝图路由
@app01.route('/app01index/')
def app01_index():

    return 'app01 index ...'



