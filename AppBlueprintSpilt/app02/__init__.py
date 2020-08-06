# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/31 15:09

from app02 import models  # 如果不导入这个,无法生成迁移文件
from app02.views import app02

# 注册蓝图到app,进行路由规划
def init_blue_app02(app):

    app.register_blueprint(app02, url_prefix="/app02/")

