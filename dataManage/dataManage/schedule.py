#coding: utf-8
from dbModels import data,user,msgToUser
from dbConnect import db_session
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import datetime,time
class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'dataManage.schedule:sendMesseges',
            'args': (),
            'trigger': 'interval',
            'seconds': 10
        }
    ]

    SCHEDULER_VIEWS_ENABLED = True
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20},
        'processpool': {'type': 'processpool','max_workers': 5}

    }



def hello():
    print findDatasDueReturned()

def findDatasDueReturned():
    selectedDatas = db_session.query(data).filter(
        data.supposedReturnTime < datetime.datetime.now().strftime('%Y-%m-%d')
    ).all()
    return selectedDatas
def sendMesseges():
    for selecteddata in findDatasDueReturned():
        name = db_session.query(user).filter(
            user.userId == selecteddata.borrowerId
        ).one().name
        new_msg = msgToUser(
            "您好， " + name +": \n 您借的资料《" + selecteddata.dataName + "》到期了，请及时归还"
                                                                       "\n （本消息由系统自动发送）",
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            selecteddata.borrowerId,
            False
        )
        db_session.add(new_msg)
        db_session.commit()
        print "发送成功"
        time.sleep(3)