#coding: utf-8
"""
This script runs the dataManage application using a development server.
"""


from os import environ
from dataManage import app
from dataManage.dbConnect import init_db
from dataManage import models_import_admin
#转换字符，确保中文参数可以传到前端页面,字符编码相关
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    """
    init the database
    """
    init_db()
    models_import_admin()
    #'thread' = True  多线程。 确保服务器在崩溃的时候有新线程产生，不会宕机
    app.run(debug = True,threaded=True)


