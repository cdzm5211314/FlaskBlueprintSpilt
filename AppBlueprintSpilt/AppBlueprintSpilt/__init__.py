# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/31 15:07

from flask import Flask
from AppBlueprintSpilt.extends import init_extends
from AppBlueprintSpilt.settings import envs
from apis import init_api
from app01 import init_blue_app01
from app02 import init_blue_app02
# from app01 import models  # 注: 不导入models,应该无法生成迁移文件,或直接在app01的init中导入
# from app02 import models  # 注: 不导入models,应该无法生成迁移文件,或直接在app01的init中导入


def create_app(env):

    app = Flask(__name__)

    # URI格式: 数据库+驱动://用户名:密码@主机:端口/具体链接哪个库
    # SQLAlchemy配置参数: 设置链接数据库的URI
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
    # SQLAlchemy配置参数: 设置sqlalchemy自动更新跟踪数据库
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    ## 注意加载配置信息与初始化第三方库的顺序

    # 加载配置参数信息
    app.config.from_object(envs.get(env))

    # 初始化第三方库
    init_extends(app)

    # 初始化蓝图 - 路由规划
    init_blue_app01(app)
    init_blue_app02(app)

    # 初始化restful-api - 路由规划
    init_api(app)

    return app
