#coding:utf-8
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2, json

class weixinTokenTool(object):
    '''向微信服务器获取token、ticket等各种访问通行证'''
    def getAccessToken(self):
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx52026669f7ddcad4&secret=f9e7b2f4cf76e2951e5ebfcb3817b89b"
        response = urllib2.urlopen(url, timeout=20)
        content=response.read()
        contentObj = json.loads(content)
        return contentObj["access_token"]
    
    def getJsapiTicket(self,accessToken):
        url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token="+ accessToken +"&type=jsapi"
        response = urllib2.urlopen(url, timeout=20)
        content=response.read()
        contentObj = json.loads(content)
        return contentObj["ticket"]

'''
{
"errcode":0,
"errmsg":"ok",
"ticket":"bxLdikRXVbTPdHSM05e5u5sUoXNKd8-41ZO3MhKoyN5OfkWITDGgnr2fwJ0m9E8NYzWKVZvdVtaUgWvsdshFKA",
"expires_in":7200
}
'''
