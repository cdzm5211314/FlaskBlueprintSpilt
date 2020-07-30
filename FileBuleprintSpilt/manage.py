# -*- coding:utf-8 -*-

from flask import Flask
from flask_script import Manager
from app01view import app01
from app02view import app02

# 创建Flask框架服务
app = Flask(__name__)

# 3.注册蓝图对象
# 第一个参数: 蓝图对象
# 第二个参数: url_prefix参数默认值是根路由,如果指定:会在蓝图注册的路由url中添加前缀
# app.register_blueprint(app01)
app.register_blueprint(app01, url_prefix='/app01/')
app.register_blueprint(app02, url_prefix='/app02/')

# 创建脚本命令行工具
manager = Manager(app=app)

# @app.route("/")
# def index():
#
#     return "Hello World!"


if __name__ == '__main__':

    # app.run()
    manager.run()

# 终端启动命令: python manage.py runserver -r -d

