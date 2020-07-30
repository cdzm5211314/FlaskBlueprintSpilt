# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 10:51

from .one_blue import oneblue
from .two_blue import twoblue


# 3.注册蓝图到app中
def init_views(app):

    app.register_blueprint(oneblue, url_prefix='/oneblue/')
    app.register_blueprint(twoblue, url_prefix='/twoblue/')
