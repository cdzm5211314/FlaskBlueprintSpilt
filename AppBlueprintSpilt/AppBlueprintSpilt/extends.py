# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/31 15:08

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# ORM映射及数据库迁移
def init_extends(app):

    db.init_app(app)
    migrate.init_app(app, db)



