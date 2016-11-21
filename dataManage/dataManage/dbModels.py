#coding: utf-8
from sqlalchemy import Column, String,Integer,Date,Boolean,DateTime,Text,Float
from dataManage.dbConnect import Base


ISOTIMEFORMAT = '%Y-%m-%d %X'
class user(Base):
    __tablename__ = 'user'

    userId = Column(Integer(),primary_key = True)
    userName = Column(String(16))
    password = Column(String(16))
    name = Column(String(30))
    def __init__(self,userName = None,
                 password = None,name = None):
        self.userName = userName
        self.password = password
        self.name = name
    def __repr__(self):
        return '<user %r>' % (self.userName)
class manager(Base):
    __tablename__ = 'manager'

    managerId = Column(Integer(),primary_key = True)
    userName = Column(String(10),nullable = False)
    password = Column(String(16),nullable = False)

    def __init__(self,userName = None,password = None):
        self.userName = userName
        self.password = password

class data(Base):
    __tablename__ = 'data'

    dataId = Column(Integer(),primary_key = True)
    dataName = Column(String(16),nullable = False)
    dataDescription = Column(Text(),nullable = True)
    dataAuthor = Column(String(30),nullable = True)
    dataPress = Column(String(30),nullable = True)
    dataLocation = Column(String(30),nullable = True)
    borrowStatus = Column(Boolean(),nullable = False,default=False)
    borrowTime = Column(Date(),nullable = True)
    supposedReturnTime = Column(Date,nullable = True)
    borrowerId = Column(Integer(),nullable = True)
    dataPrice = Column(Float(),nullable = True)
    def __init__(self,dataName = None,dataPrice = None,
                 borrowStatus = False,dataLocation = None,
                 borrowTime = None,supposedReturnTime = None,
                 borrowerId = None,dataDescription = None,
                 dataAuthor = None,dataPress = None):
        self.dataName = dataName
        self.dataAuthor = dataAuthor
        self.dataPress = dataPress
        self.borrowStatus =borrowStatus
        self.borrowTime = borrowTime
        self.supposedReturnTime = supposedReturnTime
        self.borrowerId = borrowerId
        self.dataDescription = dataDescription
        self.dataLocation = dataLocation
        self.dataPrice = dataPrice
class msgToUser(Base):
    __tablename__ = 'msgtouser'

    msgId = Column(Integer(),primary_key = True)
    msgTitle = Column(String(30))
    msgContent = Column(Text(),nullable = True)
    sendTime = Column(DateTime(),nullable = False)
    userId = Column(Integer(),nullable = False)
    readStatus = Column(Boolean(),nullable = False,default=False)
    sender = Column(String(30),nullable = False,default = '系统')

    def __init__(self,msgTitle = None,
                 msgContent = None,sendTime = None,
                 userId = None,readStatus = False,
                 sender = None,
                 ):
        self.msgTitle = msgTitle
        self.msgContent = msgContent
        self.sendTime = sendTime
        self.userId = userId
        self.readStatus = readStatus
        self.sender = sender