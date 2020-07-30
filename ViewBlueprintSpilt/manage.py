# -*- coding:utf-8 -*-

# from flask import Flask
import os

from flask_migrate import MigrateCommand
from flask_script import Manager
from FirstApp import create_app

# 加载flask配置环境信息
env = os.environ.get('FLASK_ENV', 'develop')

# 创建Flask框架服务
# app= Flask(__name__)
# app = create_app()
app = create_app(env)

# 创建脚本命令工具管理器
manager = Manager(app=app)

# 数据库迁移命令添加到脚本管理器中
manager.add_command('db', MigrateCommand)

# @app.route("/")
# def index():
#
#     return "Hello World!"


if __name__ == '__main__':

    # FirstApp.run()
    manager.run()

# 终端命令行: python manage.py runserver -r -d

