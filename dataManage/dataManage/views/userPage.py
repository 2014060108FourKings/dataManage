#coding: utf-8
from flask import render_template,Blueprint,json,request,session
from dataManage.dbConnect import db_session
from dataManage.dbModels import *
userPage = Blueprint('userPage',__name__)

@userPage.route('/userLogin')
def userLogin():
    return render_template('userPage/userLogin.html',
                           title = '登录')

@userPage.route('/signIn',methods=['POST','GET'])
def signIn():
    if request.method == 'POST':
        loginData = json.loads(request.form.get('data'))
        msg = ''
        userName_input = loginData['userName']
        password_input = loginData['password']
        users = db_session.query(user).filter(user.userName==userName_input).all()
        if users == []:
            msg = 'user not exists'
        else:
            checkedUser = users[0]
            if checkedUser.password == password_input:
                session['name'] = checkedUser.name
                session['currentUserId'] = checkedUser.userId
                msg = 'success'
            else :
                msg = 'passwordError'
        return  str(msg)
    else:
        return '哥们你又乱输网址。。。。。'
@userPage.route('/userLogout')
def userLogout():
    session['name'] = None
    session['currentUserId'] = None
    return "<script>window.location = '/'</script>"

@userPage.route('/userInfoView')
def userInfoView():
    if 'currentUserId' not in session or session['currentUserId'] == None:
        return "<script>window.location = '/userLogin'</script>"
    else:
        currentUserId = session['currentUserId']
        currentUser = db_session.query(user).filter(user.userId == currentUserId).one()
        return render_template('userPage/userInfoView.html',title = '个人信息',user = currentUser)
@userPage.route('/userRegister')
def userRegister():
    return render_template('userPage/userRegister.html',title = '用户注册')

@userPage.route('/reg',methods = ['POST','GET'])
def reg():
    if request.method == 'POST':
        registerData = json.loads(request.form.get('data'))
        msg = ''
        userName_input = registerData['userName']
        password_input = registerData['password']
        name_input = registerData['name']
        users = db_session.query(user).filter(user.userName==userName_input).all()
        if users == []:
            newUser = user(userName = userName_input,password = password_input,name = name_input)
            db_session.add(newUser)
            db_session.commit()
            db_session.close()
            msg = 'success'

        else:
            msg = '用户名已被注册'
        return  str(msg)
    else:
        return '哥们你又乱输网址。。。。。'