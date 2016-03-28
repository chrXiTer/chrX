#coding:utf-8
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import random
import urllib2 
import time

class linkDownloadTool(object):
    '''下载某链接内容，并处理、保存、发布等'''
        
    def __dealImgUrlInWeixin(self, content):
        '''对链接中内容对应的图片链接进行处理（因为图片会保持到自己服务器，内容中的图片地址需要进行改变'''
        imgUrls = []
        imgUrlPrefix = str(long(time.time() * 1000)) + "-" + str(random.randint(10000, 99999)) + "/"
        imgUrlNo = [1]
        def repl(matchobj):
            weixinUrls = matchobj.group(1) 
            localUrls =  imgUrlPrefix + str(imgUrlNo[0])
            imgUrlNo[0] = imgUrlNo[0] + 1
            imgUrls.append({'weixinUrls': weixinUrls, 'localUrls': localUrls})
            return 'src="http://h5jc.sinaapp.com/weixinimg/' + localUrls + '"'
        content = re.sub(r'data-src="([^"]+)"', repl, content) # re.sub(r'data-src="([^"]*)"', r'src="\1"', content) #
        return (imgUrls, content)

    def __downloadAFile(self, url, saveFileNameWithPath, imgSaveFunc):
        '''根据一个链接，将对应的文件（主要是图片）下载下来并保存'''
        response = urllib2.urlopen(url, timeout=20)
        content = response.read()
        contenType = response.info().gettype()
        imgSaveFunc(saveFileNameWithPath, content, contenType)

    def getLinkContent(self, url, contentSaveFunc, imgSaveFunc):
        '''下载某链接内容,并调用内容保存函数进行保存。链接内容中所引的图片，也会下载下来'''
        response = urllib2.urlopen(url, timeout=20)
        content = response.read()
        content = content.decode('utf-8')
        pattern = re.compile(r'(<div id="js_article" class="rich_media">.*?)<div id="js_pc_qr_code" class="qr_code_pc_outer"', re.M | re.S)
        match = pattern.search(content)
        if match:
            content = match.group(1) + '</div></div>'
        [imgUrls, content] = self.__dealImgUrlInWeixin(content) 
        content = content.encode('utf-8')
        contentSaveFunc(content)
        for imgUrl in imgUrls:
            self.__downloadAFile(imgUrl["weixinUrls"], imgUrl["localUrls"], imgSaveFunc)