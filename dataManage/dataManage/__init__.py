#coding: utf-8
"""
The flask application package.
"""
from flask import Flask
from views.homePage import homePage
from views.userPage import userPage
from views.managerPage import managerPage
from views.dataPage import dataPage
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from dbModels import *
from dataManage.dbConnect import db_session
from schedule import Config

app = Flask(__name__)
app.register_blueprint(homePage)
app.register_blueprint(userPage)
app.register_blueprint(managerPage)
app.register_blueprint(dataPage)
app.config.from_object('dataManage.config')
app.config.from_object(Config())
admin = Admin(app, name='高校资料管理系统', template_mode='bootstrap3')
def models_import_admin() :
    admin.add_view(ModelView(user,db_session))
    admin.add_view(ModelView(manager,db_session))
    admin.add_view(ModelView(data,db_session))
    admin.add_view(ModelView(msgToUser,db_session))

