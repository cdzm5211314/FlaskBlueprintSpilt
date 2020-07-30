# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 10:48

from flask import Flask
# from FirstApp.views import init_route
# from FirstApp.views.one_blue import oneblue
# from FirstApp.views.two_blue import twoblue
# from FirstApp.views import oneblue, twoblue
# from FirstApp.models import init_models
from FirstApp.settings import envs
from FirstApp.views import init_views
from FirstApp.extend import init_extend


# 注: app创建时会从Flask注册函数中读取template_folder，如果没有设置，默认是app/templates，作为全局jinja_loader
# def create_app():
def create_app(env):
    # 创建Flask框架服务
    app = Flask(__name__)

    # 懒加载方式加载路由
    # init_route(app)

    # 注册蓝图方式加载路由
    # 第一个参数: 蓝图对象
    # 第二个参数: url_prefix参数默认值是根路由,如果指定:会在蓝图注册的路由url中添加前缀
    # app.register_blueprint(oneblue)

    # app.register_blueprint(oneblue, url_prefix='/oneblue/')
    # app.register_blueprint(twoblue, url_prefix='/twoblue/')

    # URI格式: 数据库+驱动://用户名:密码@主机:端口/具体链接哪个库
    # 使用sqlite数据库
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
    # 使用MySQL数据库
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/flaskexample"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # 使用类形式加载配置信息
    # app.config.from_object(envs.get('develop'))
    app.config.from_object(envs.get(env))

    # 加载模型
    # init_models(app)

    # 加载第三方库
    init_extend(app)

    # 加载蓝图
    init_views(app)

    return app
