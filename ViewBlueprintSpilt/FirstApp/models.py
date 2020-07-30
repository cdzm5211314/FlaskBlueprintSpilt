# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2020-05-02 10:37

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
# def init_models(app):
#     db.init_app(app=app)


from FirstApp.extend import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))

    def save(self):
        db.session.add(self)
        db.session.commit()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))