# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 12:29


from flask import Blueprint

# 创建蓝图对象
# 第一个参数表示蓝图的名字,第二个参数表示当前模块
# 注: 实际开发中,蓝图对象与蓝图名字一般保持一致
twoblue = Blueprint("twoblue", __name__)


# 使用蓝图对象定义路由
@twoblue.route("/twoindex/")
def two_index():

    return "two index ..."
