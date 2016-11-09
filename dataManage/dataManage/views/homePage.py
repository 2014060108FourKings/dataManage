#coding: utf-8
from datetime import datetime
from flask import render_template,Blueprint
from dataManage.dbConnect import db_session
from dataManage.dbModels import data

homePage = Blueprint('homePage',__name__)
@homePage.route('/')
@homePage.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'homePage/index.html',
        title='主页',
        year=datetime.now().year,
    )

@homePage.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'homePage/contact.html',
        title='其他',
        year=datetime.now().year,
        message='Your contact page.'
    )



