#coding: utf-8
from flask import render_template,Blueprint,request
from dataManage.dbConnect import db_session
from dataManage.dbModels import data

import  datetime

dataPage = Blueprint('dataPage',__name__)

@dataPage.route('/datasView')
def datasView():
    datas = db_session.query(data).filter().all()
    return render_template(
        'dataPage/datasView.html',
        title='资料浏览',
        datas = datas
    )
@dataPage.route('/dataSearch',methods = ['GET'])
def dataSearch():
    if request.args.get('searchContent') != None:
        searchContent = str(request.args.get('searchContent'))
        print str('%'+searchContent[1:-1]+'%')
        """
        前端传来的searchContent为字符串，带双引号，下面[1:-1]是将开头双引号去除
        """
        datas = db_session.query(data).filter(
            data.dataName.like('%'+searchContent[1:-1]+'%')
        ).all()
        return render_template(
            'dataPage/datasView.html',
            title=str(searchContent+'的相关搜索'),
            datas=datas
        )
    else:
        return "<script>alert('非法操作');" \
               "window.location='/'</script>"

@dataPage.route('/dataInfo/<dataId>')
def dataInfo(dataId):
    currentData = db_session.query(data).filter(data.dataId == dataId).one()
    return render_template('dataPage/dataInfo.html',currentData = currentData,title = currentData.dataName,
                           currentDate = datetime.datetime.now().strftime('%Y-%m-%d'),
                           supposedReturnDate = (datetime.datetime.now()+datetime.timedelta(15)).strftime('%Y-%m-%d') )


@dataPage.route('/dataBorrow',methods=['POST','GET'])
def dataBorrow():
    if request.method == 'POST':
        bId = request.form['borrowerId']
        dId = request.form['dataId']
        try:
            db_session.query(data).filter(data.dataId == dId ).update(
                {'borrowerId': bId,
                 'borrowStatus':True,
                 'borrowTime': datetime.datetime.now().strftime('%Y-%m-%d'),
                 'supposedReturnTime':(datetime.datetime.now()+datetime.timedelta(15)).strftime('%Y-%m-%d')
                 }
            )
            db_session.commit()
            return "<script>alert('恭喜，借阅成功！');window.location = '/datasView' </script>"
        except Exception,exp:
            return str(exp)
    else :
        return "哥们，你别乱输网址啊。"
@dataPage.route('/dataRenew',methods = ['POST','GET'])
def dataRenew():
    if request.method == 'POST':
        dId = request.form['dataId']
        try:
            db_session.query(data).filter(data.dataId == dId ).update(
                {
                 'supposedReturnTime':(datetime.datetime.now()+datetime.timedelta(15)).strftime('%Y-%m-%d')
                 }
            )
            db_session.commit()
            return "<script>alert('恭喜，续借成功！');window.location = '/datasView' </script>"
        except Exception,exp:
            return str(exp)
    else :
        return "哥们，你别乱输网址啊。"
@dataPage.route('/dataReturn',methods = ['POST','GET'])
def dataReturn():
    if request.method == 'POST':
        dId = request.form['dataId']
        try:
            db_session.query(data).filter(data.dataId == dId ).update(
                {
                     'supposedReturnTime': None,
                     'borrowTime':None,
                     'borrowStatus': False,
                     'borrowerId': None,
                 }
            )
            db_session.commit()
            return "<script>alert('恭喜,还书成功！');window.location = '/datasView' </script>"
        except Exception,exp:
            return str(exp)
    else :
        return "哥们，你别乱输网址啊。"



