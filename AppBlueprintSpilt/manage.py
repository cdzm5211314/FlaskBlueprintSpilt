# from flask import Flask
import os

from flask_migrate import MigrateCommand
from flask_script import Manager
from AppBlueprintSpilt import create_app

# 加载flask配置环境信息
env = os.environ.get('FLASK_ENV', 'develop')

# app = Flask(__name__)
app = create_app(env)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    manager.run()

# 终端命令行: python manage.py runserver -r -d