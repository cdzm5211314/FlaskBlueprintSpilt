# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/31 15:09

from app01 import models  # 如果不导入这个,无法生成迁移文件
from app01.views import app01

# 注册蓝图到app,进行路由规划
def init_blue_app01(app):

    app.register_blueprint(app01, url_prefix="/app01/")


