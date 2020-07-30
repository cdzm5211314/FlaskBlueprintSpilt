# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/7/30 12:29


from flask import Blueprint, render_template
# from FirstApp.models import db
# from FirstApp.views.extend import db  # 同下方式
from FirstApp.models import db, User


# 1.创建蓝图对象
# 第一个参数表示蓝图的名字,第二个参数表示当前模块
# 注: 实际开发中,蓝图对象与蓝图名字一般保持一致
oneblue = Blueprint("oneblue", __name__)


# 2.使用蓝图对象定义路由
@oneblue.route("/oneindex/")
def one_index():

    # return "one index ..."
    return render_template("oneindex.html", msg="填充数据")

# 蓝图对象定义路由 - 使用程序创建数据库
@oneblue.route('/create_database/')
def create_database():

    db.create_all()

    return "数据库创建成功!!!"


# 蓝图对象定义路由 - 使用程序删除数据库
@oneblue.route('/drop_database/')
def drop_database():

    db.drop_all()

    return "数据库删除成功!!!"


@oneblue.route('/adduser/')
def add():

    user = User()
    user.username = "徐六"

    # db.session.add(user)
    # db.session.commit()

    user.save()

    return "添加用户成功..."