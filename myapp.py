#coding:utf-8
from __future__ import unicode_literals
import sys, re
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, request, url_for
from flask import redirect, make_response

app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

##########  工具函数 ##########################
def htmlFileToString(path):
    file_object = open(path)
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
    return all_the_text

##########  全站静态资源路由 #####################
@app.route('/static/<path:other>')
def staticResouce(other):
    return static_file(other, root='static')

@app.route('/js/<path:jsFile>')
def chrX_jsFile(jsFile):
    return static_file(jsFile, root='static/chrX/js')

#####################################
@app.route('/')
@app.route('/mainData')
def toMain1():
    return redirect("/mainData/index")

@app.route('/mainData/<path:other>')
def data1(other=None):
    if other == None:
        path = "./static/mainData/index.html"
    ##########  红黑树 ##### 游戏 #####
    elif re.search("(\.js$)|(\.css$)|(\.html$)|(\.png$)|(\.jpg$)|(\.gif$)|(\.manifest$)", other):
        path = 'mainData/' + other
        return app.send_static_file(path)
    else:
        path = "./static/mainData/" + other[0: -4] + ".html"
    dataHtmlStr = htmlFileToString(path)
    
    response = make_response(str(dataHtmlStr))
    #response.headers['cache-control'] = 'max-age=315360000'
    #response.headers['etag'] = 'max-age=315360000'
    return response
########################################################################### 
@app.route('/mainData/index')
@app.route('/mainData/tool')
@app.route('/mainData/about')
@app.route('/mainData/jsTool/jsTool')
def main1(other=None):
    layoutStr = htmlFileToString("./static/templet/layout.html")
    return layoutStr
    
@app.route('/mainData/rbTree')
def toMain2(other=None):
    return redirect("/mainData/rbTree/rbTree")
        
@app.route('/mainData/rbTree/rbTree')
@app.route('/mainData/rbTree/rbTreeDemo')
def main2(other=None):
    layoutStr = htmlFileToString("./static/templet/layout_rbTree.html")
    return layoutStr
    
@app.route('/mainData/game')
def toMain3(other=None):
    return redirect('/mainData/game/woodGame')
    
@app.route('/mainData/game/fishSwimGame')
@app.route('/mainData/game/woodGame')
def main3(other=None):
    layoutStr = htmlFileToString("./static/templet/layout_game.html")
    return layoutStr
       
'''
@app.route('/tool/uploadFile', method='POST')
def toolPost():
    uploadFile = request.files.get('upload')
    from sae.storage import Bucket, Connection
    #c = Connection(accesskey='xw2oozj4zw', secretkey='l2kzjwzzl5w115yjy2mkk54ymwmml20j44z5yk1k', account='chrX')
    #bucket = c.get_bucket('uploadfiles')
    bucket = Bucket('uploadfiles')
    bucket.put_object(uploadFile.filename, uploadFile.file)
    return 'uploatOK: ' + bucket.generate_url(uploadFile.filename)
'''

########################################################################### 
@app.route('/h5jc')
def toH5jc():
    return redirect("/static/h5jcData/html/html_intro.htm")
    
@app.route('/webLink')
def webLink():
    return redirect('static/webLink/webLink.html')


    
    

###############################################
#
#   微信消息处理
#
###############################################

import weixin.weixinMessageTool as weixinMessageTool
import weixin.saeStorage as saeStorage
import weixin.tokenTool as tokenTool

tokenObj = tokenTool.tokenTool()

@app.route('/weixin', methods=['GET', 'POST'])
def weixin():
    if request.method == 'GET':
        returnStr = request.args.get('echostr')
    else:
        strReceived = request.data
        messageHandler = weixinMessageTool.MessageHandler()
        returnStr = messageHandler.handleMessage(strReceived)
    if returnStr == None:
        returnStr = "weixin"
    return returnStr

@app.route('/getConfigSignatureInfo')
def getConfigSignatureInfo():
    url = request.args.get('url')
    resultJsonStr = tokenObj.getSignatureInfo(url)
    return ';callback('+ resultJsonStr + ');'
    
@app.route('/weixinimg/<path:name>')
def getWeixinImg(name):
    saeStorageObj = saeStorage.saeStorage("weixinimg")
    url=saeStorageObj.getUrl(name)
    return redirect(url)
    

###############################################
@app.route('/getWeiXinAccessToken')
def getWeiXinAccessToken():
    return tokenObj.getWeiXinAccessToken()

@app.route('/getWeixinJsapiTicket')
def getWeixinJsapiTicket():
    return tokenObj.getWeixinJsapiTicket()