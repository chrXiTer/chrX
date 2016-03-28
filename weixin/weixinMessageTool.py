#coding:utf-8
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xml.dom.minidom, time
import threading as threadingCx

import messageHandler.databaseMessageTool as databaseMessageTool
import messageHandler.linkDownloadTool as linkDownloadTool

class MessageHandler(object):
    def handleMessage(self,message):
        '''处理接收到的xml微信消息,并返回最终的xml消息回复'''
        self.__databaseObj = databaseMessageTool.databaseTool()
        self.__messageReceived = message
        self.__itemsReceive = self.__parseReceivedXmlStringToItems()
        self.__saveMessage()
        messageType = self.__itemsReceive['MsgType']
        if messageType == 'text':
            returnStr = self.__dealTextMessage()
        elif messageType == 'link':
            returnStr = self.__dealLinkMessage()
        elif messageType == 'image':
            returnStr =self.__dealImageMessage()
        else:
            pass
        return returnStr

    def __parseReceivedXmlStringToItems(self):
        '''将收到的xml格式消息转换为python的字典项'''
        dom = xml.dom.minidom.parseString(self.__messageReceived)
        tagNameList = ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType',   'MsgId']
        msgTypeE = dom.getElementsByTagName('MsgType')[0];
        msgType = str(msgTypeE.childNodes[0].data)
        if msgType == 'text':
            tagNameList.append('Content')
        elif msgType == 'link':
            tagNameList.extend(['Title', 'Description', 'Url'])
        elif msgType == 'image':
            tagNameList.extend(['PicUrl', 'MediaId'])
        else:
            pass
        items = {}
        for tagName in tagNameList:
            element = dom.getElementsByTagName(tagName)[0]
            items[tagName] = str(element.childNodes[0].data)
        return items

    def __saveMessage(self):
        '''将消息保存到数据库中'''
        self.__databaseObj.saveMessage(self.__itemsReceive['FromUserName'], self.__messageReceived)

    def __dealTextMessage(self):
        '''分析【文本】消息的具体内容，并给出对应的结果（回应）消息。'''
        if self.__itemsReceive['Content'] == '知县':
            return self.__createTextMessageToSend('<a href="http://zhixian001.applinzi.com'+''+'">点击进入知县网>></a> ')
        elif self.__itemsReceive['Content'] == '游戏':
            return self.__createTextMessageToSend('<a href="http://zhixian001.applinzi.com/Home/Entertainment/AllGameList'+''+'">点击开始玩游戏>></a> ')
        elif self.__itemsReceive['Content'] == '新消息':
            return self.__createTextMessageToSend('<a href="http://zhixian001.applinzi.com/Home/News'+''+'">点击查看最新消息>></a> ')
        else:
            return self.__createTextMessageToSend(
                '感谢使用知县订阅号:\n'
                +'    输入 【知县】 获取知县网地址\n'
                +'    输入 【游戏】 获取游戏地址\n'
                +'    输入 【新消息】 获取最新消息'
                +'    输入 【帮助】 获取帮助信息\n'
            )

    def __dealLinkMessage(self):
        '''分析【链接】消息的具体内容，并给出对应的结果（回应）消息。'''
        def getLinkContent():
            url = self.__itemsReceive["Url"]
            title = self.__itemsReceive["Title"]
            userOpenId = self.__itemsReceive["FromUserName"]
            contentSaveFunc  = lambda content:self.__databaseObj.saveLinkContentToNews(userOpenId, title, content)
            def imgSaveFunc(saveFileNameWithPath, content, contenType):
                saeStorageObj = saeStorage.saeStorage("weixinimg")
                saeStorageObj.save(saveFileNameWithPath, content, contenType)
            linkDownLoadObj = linkDownloadTool.linkDownloadTool()
            linkDownLoadObj.getLinkContent(url, contentSaveFunc, imgSaveFunc)
        t = threadingCx.Thread(target=getLinkContent, name='getLinkContentThread')
        t.start()
        return self.__createTextMessageToSend('感谢分享微信链接')

    def __dealImageMessage(self):
        '''分析【链接】消息的具体内容，并给出对应的结果（回应）消息。'''
        return self.__createTextMessageToSend('感谢分享图片')

    def __createTextMessageToSend(self, messageText):
        '''根据需要回复的【文本】消息内容，创建具体的xml格式的微信消息回复'''
        tagNameList = ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'Content']
        valueList = {
            'FromUserName':self.__itemsReceive['ToUserName'],
            'ToUserName':self.__itemsReceive['FromUserName'],
            'CreateTime':str(time.time())[0:-3],
            'MsgType':'text',
            'Content':messageText
        }
        doc = xml.dom.minidom.Document()  #创建DOM文档对象
        XmlStringSend = doc.createElement('xml') #创建根元素
        doc.appendChild(XmlStringSend)

        def createChildNode(tagName):
            if(tagName == 'CreateTime'): #子节点为TextNode
                result = doc.createTextNode(valueList[tagName])
            else:  #子节点为CDATASection
                result = doc.createCDATASection(valueList[tagName])
            return result

        for tagName in tagNameList:
            element = doc.createElement(tagName)
            childNode = createChildNode(tagName)
            element.appendChild(childNode)
            XmlStringSend.appendChild(element)
        return XmlStringSend.toxml()
        
