#coding: utf-8
class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'dataManage.schedule:hello',
            'args': (),
            'trigger': 'interval',
            'seconds': 10
        }
    ]

SCHEDULER_VIEWS_ENABLED = True

def hello():
    print 'hello'