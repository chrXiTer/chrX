#coding:utf-8
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, text

from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
    MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB,
)

class databaseTool(object):
    def __init__(self):
        #connectStrLocal = b"mysql://" + MYSQL_USER + ":" + MYSQL_PASS + "@" + MYSQL_HOST + ":" + MYSQL_PORT + "/" + MYSQL_DB + "?charset=utf8"
        connectStrForeign = b"mysql://" + '1wl13z0zmj' + ":" + 'jm34iz52x44k1wkwhj43055ixmmij44jki103ii2' + "@" + MYSQL_HOST + ":" + MYSQL_PORT + "/app_zhixian001?charset=utf8"
        connectStrLocal = connectStrForeign  #由于SAE的mysql不再提供免费额度，本站mysql数据库已经删除，采用外部数据库
        #print connectStrForeign
        self.__engineLocal = create_engine(connectStrLocal, encoding=b"utf-8", echo=True)
        self.__engineForeign = create_engine(connectStrForeign, encoding=b"utf-8", echo=True)
        
        metadata = MetaData()
        userMessage = Table('userMessage', metadata, 
            Column('id', Integer, primary_key=True),
            Column('user', String(30)),
            Column('message', String(3000)),
        )
        metadata.create_all(self.__engineLocal) #创建数据表，如果数据表存在，则忽视
        
    def saveMessage(self, user, message):
        conn = self.__engineLocal.connect()
        sqlStr = text("INSERT INTO userMessage(user, message) VALUES(:user, :message)", {
            "user":user,
            "message":message
        })
        result = conn.execute(sqlStr)
        return "OK" + str(result)
        
    def saveLinkContentToNews(self, userOpenId, title, content):
        conn = self.__engineForeign.connect()
        county = "hengyangxian"
        publisherId = self.getUserIdFromWeixinOpenId(userOpenId)
        if publisherId == None:
            publisherId = self.addUserWithWeixinOpenId(userOpenId)
        if publisherId == None:
            return "error 向数据库添加数据失败"
        print('chrX ___')
        print(publisherId)
        tableName = "cx_x_" + county + "_news"
        sqlStr = text("INSERT INTO "+ tableName + "(Title, Content,PublisherId) VALUES(:title, :content, :publisherId)")
        result = conn.execute(sqlStr,  title = title, content = content, publisherId = publisherId)
        return "OK" + str(result)
    
    def getUserIdFromWeixinOpenId(self, openId):
        conn = self.__engineForeign.connect()
        sqlStr = "SELECT UserId FROM cx_user_foreign_id WHERE WeixinOpenId = '" + openId + "'"
        result = conn.execute(sqlStr)
        firstRow = None
        firstRow = result.first()
        if firstRow == None:
            return None
        else:
            return firstRow['UserId']
    
    def addUserWithWeixinOpenId(self, openId):
        conn = self.__engineForeign.connect()
        sqlStr = text("INSERT INTO cx_user(UserName, Password, county) VALUES(:UserName, :Password, :county)")
        result = conn.execute(sqlStr,  UserName = '#$微信用户$#', Password = '#$weixinPassword$#', county='hengyangxian')
        if result == None:
            print("chrX error:exexute sql fail. " + sqlStr)
            return None
        else:
            UserId = result.lastrowid
        sqlStr2 = text("INSERT INTO cx_user_foreign_id(UserId, WeixinOpenId) VALUES(:UserId, :weixinOpenId)")
        result2 = conn.execute(sqlStr2, UserId = UserId, weixinOpenId = openId)
        if result2 == None:
            print("chrX error:exexute sql fail. " + sqlStr2)
            return None
        else:
            return result2.lastrowid
