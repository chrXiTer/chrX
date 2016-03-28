#coding:utf-8
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from sqlalchemy import create_engine, Table, Column, Integer, BigInteger, String, MetaData, ForeignKey, text
from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
    MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
)

class databaseTokenTool(object):
    '''从数据库获取token、ticket等各种访问通行证，以及向数据库添加、更新这些访问通行证'''
    def __init__(self):
        #connectStr = b"mysql://"+ MYSQL_USER + ":" + MYSQL_PASS + "@" + MYSQL_HOST + ":" + MYSQL_PORT + "/" + MYSQL_DB + "?charset=utf8"
        connectStrForeign = b"mysql://" + '1wl13z0zmj' + ":" + 'jm34iz52x44k1wkwhj43055ixmmij44jki103ii2' + "@" + MYSQL_HOST + ":" + MYSQL_PORT + "/app_zhixian001?charset=utf8"
        connectStr = connectStrForeign  #由于SAE的mysql不再提供免费额度，本站mysql数据库已经删除，采用外部数据库
        self.__engine = create_engine(connectStr, encoding=b"utf-8", echo=True)
        metadata = MetaData()
        accessToken = Table('accessToken', metadata,
                Column('Id', Integer, primary_key=True),
                Column('Value', String(300)),
                Column('DataTime', BigInteger),
            )
        metadata.create_all(self.__engine) # 创建数据表，如果数据表存在，则忽视
        
    def __getWeixinAToken(self, tokenRecordId):
        conn = self.__engine.connect()
        sqlStr = text("SELECT Value, DataTime FROM accessToken WHERE Id=:Id")
        result = conn.execute(sqlStr, Id = tokenRecordId)
        #result == None 不会在执行select后出现
        firstRow = result.fetchone()
        if firstRow == None: #没有相应数据
            return None
        dataTime = firstRow["dataTime"]
        if long(time.time()) - dataTime > 7000 or firstRow["Value"] == None:  #数据值过期（过期时间为7200），或者数据错误（为空）
            sqlStr = text("DELETE FROM accessToken WHERE Id=:Id")
            result = conn.execute(sqlStr, Id = tokenRecordId)
            return None
        else:
            return firstRow["Value"]
    
    def __updateWeixinToken(self, tokenRecordId, tokenValueStr):
        conn = self.__engine.connect()
        sqlStr = text("INSERT INTO accessToken(Id, Value, DataTime) VALUES(:Id, :Value, :DataTime)")
        t = long(time.time())
        result = conn.execute(sqlStr, Id = tokenRecordId, Value = tokenValueStr, DataTime = t)
        conn.close()

    def getWeixinAccessToken(self):
        return self.__getWeixinAToken(1)
    
    def updateWeixinAccessToken(self, accessTokenStr):
        return self.__updateWeixinToken(1, accessTokenStr)
        
    def getWeixinJsapiTicket(self):
        return self.__getWeixinAToken(2)
    
    def updateWeixinJsapiTicket(self, accessTokenStr):
        return self.__updateWeixinToken(2, accessTokenStr)
        
        