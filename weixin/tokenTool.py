#coding:utf-8
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import TokenTool.databaseTokenTool as databaseTokenTool
import TokenTool.weixinTokenTool as weixinTokenTool
import time
import random
import hashlib
import json

class tokenTool(object):
    '''给应用提供各种token及相关用token加密的信息。
    优先从databaseTokenTool中获取token；
    当databaseTookenTool中token失效时，从weixinTokenTool获取token并更新用databaseToken根系数据库中保存的token'''
    def __init__(self):
        self.__databaseTokenObj = databaseTokenTool.databaseTokenTool()

    def __random_str(self, randomlength):
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        randomStr = "".join([random.choice(chars) for i in range(0, randomlength)])
        return randomStr

    def getWeiXinAccessToken(self):
        weixinTokenObj = weixinTokenTool.weixinTokenTool()
        accessToken = self.__databaseTokenObj.getWeixinAccessToken()
        if(accessToken == None):
            accessToken = weixinTokenObj.getAccessToken()
            self.__databaseTokenObj.updateWeixinAccessToken(accessToken)
        return accessToken

    def getWeixinJsapiTicket(self):
        weixinTokenObj = weixinTokenTool.weixinTokenTool()
        ticket = self.__databaseTokenObj.getWeixinJsapiTicket()
        if(ticket == None):
            accessToken = weixinTokenObj.getAccessToken()
            ticket = weixinTokenObj.getJsapiTicket(accessToken)
            self.__databaseTokenObj.updateWeixinJsapiTicket(ticket)
        return ticket

    def getSignatureInfo(self, url):
        '''为一个url获取签名信息，利用该签名信息，url对应页面将能够访问微信接口'''
        jsapiTicket = self.getWeixinJsapiTicket()
        nonceStr =  self.__random_str(8)
        timestamp = str(long(time.time()))
        dd = 'd' + jsapiTicket
        ddd = 'd' + nonceStr
        dddd = 'd' + timestamp
        ddddd = 'd' + url
        strToSignature = 'jsapi_ticket=' + jsapiTicket + '&noncestr='+ nonceStr +'&timestamp='+ timestamp +'&url=' + url
        #signature =  hashlib.sha1("ssss".encode('ascii')).hexdigest()
        signature =  hashlib.sha1(strToSignature).hexdigest()
        returnDic = {'signature':signature, 'nonceStr':nonceStr, 'timestamp':timestamp}
        returnJson = json.dumps(returnDic)
        return returnJson
