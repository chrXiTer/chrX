#from pathlib import Path
import os
import re

        
def findAHtmlTag(oriStr, tagStartStr):
        '''返回html标签在字符串中的位置:包括前后连个索引，保存在元组中'''
        index1 = tagStartStr.find("<") + 1
        index2 = tagStartStr.find(" ")
        index2_1 = tagStartStr.find(" ")
        if index2_1 >= 0 and index2_1 < index2:
            index2 = index2_1
        tagName = tagStartStr[index1:index2]
        
        strIndex =  oriStr.find(tagStartStr)
        if strIndex < 0:
            return (-1, -1)
        strIndexDivH = oriStr.find('<' + tagName, strIndex + 4) #大于strIndex，小于等于tag标签头的结束
        strIndexDivR = oriStr.find('</' + tagName + '>', strIndex + 4)
        while strIndexDivH < strIndexDivR and strIndexDivH >= 0 and  strIndexDivR >= 0:
            strIndexDivH = oriStr.find('<' + tagName, strIndexDivH + 4)
            strIndexDivR = oriStr.find('</' + tagName + '>', strIndexDivR + 4)
        else:
            strIndexDivRR = oriStr.find('>', strIndexDivR) + 1
            return (strIndex, strIndexDivRR)
                
def StrDelAHtmlTag(oriStr, tagStartStr, fileName):
        divStartIndex, divEndIndex = findAHtmlTag(oriStr, tagStartStr)
        #print(divStartIndex, divEndIndex)
        if divStartIndex > 0 and divEndIndex > 0:
                deletedStr = oriStr[divStartIndex:divEndIndex]
                remainStr = oriStr[:divStartIndex] + oriStr[divEndIndex:]
        else:
                deletedStr = ""
                remainStr = oriStr
                print("fail: on delete html element start with" + tagStartStr + "*** in file " + fileName)
        return (deletedStr, remainStr)

def deletNotNeed(contentStr, fileName):
        reg =  re.compile('<html>\s<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
                                  +'\s<html xmlns="http://www.w3.org/1999/xhtml">')
        strNew = reg.sub('<!DOCTYPE html>\n<html>', contentStr)

        reg =  re.compile('<meta name="author" content="w3school.com.cn" />\s<meta name="Copyright" content="Copyright W3school.com.cn All Rights Reserved." />')
        strNew = reg.sub('', strNew)

        strNew = StrDelADiv(strNew, '<div id="header">', fileName)
        strNew = StrDelADiv(strNew, '<div id="navfirst">', fileName)
        strNew = StrDelADiv(strNew, '<div id="selected">', fileName)

        #删除内容顶部和底部的“上一节”、“下一节”块区
        reg =  re.compile('\s*<div\s+id="[tb]pn">\s*<ul class="prenext">([^<]|<[^/]|</[^u])*</ul>\s*</div>')
        strNew = reg.sub(' ', strNew)

        strNew = StrDelADiv(strNew, '<div id="sidebar">', fileName)
        strNew = StrDelADiv(strNew, '<div id="footer">', fileName)

        strNew = strNew.replace('<li><a href="index.asp.htm" tppabs="http://w3school.com.cn/css/index.asp" title="CSS 教程">CSS 教程</a></li>\n', '')
        strNew = strNew.replace(".asp.htm", ".htm")
        strNew = strNew.replace("</p>\n\n", "</p>\n")
        strNew = strNew.replace("\n\n\n", "\n\n")

        reg = re.compile('\s?tppabs="http://[^"]+"\s?')
        strNew = reg.sub(' ', strNew)

        strNew = strNew.replace("</body>", '<script src="../chrX.js"></script>\n</body>')
        return strNew

def deleteAndReturn(contentStr, DivStartStr):
    divStartIndex, divEndIndex = findADiv(contentStr, DivStartStr)
    if divStartIndex >=0 and divEndIndex >=0:
            strCommon = contentStr[divStartIndex : divEndIndex]
            strNew = contentStr[:divStartIndex] + contentStr[divEndIndex:]
            return (strNew, strCommon)
    else: return (contentStr, "")

def processADir(oriDirName, newDirNaem):
        if not os.path.isdir(oriDirName):
                print("error ./css is not a dir")
                return
        cssDir = os.listdir(oriDirName)
        oriCurDir = os.getcwd()
        commonStr = ""
        for fileName in cssDir:
                os.chdir(oriDirName)
                if not os.path.isfile(fileName):
                        print("error :" + fileName +": is not a file")
                        return
                curfile = open(fileName, 'r')
                contentStr = curfile.read();
                contentStr = deletNotNeed(contentStr, fileName)
                contentStr, strDeleted = deleteAndReturn(contentStr, '<div id="navsecond">')
                #if commonStr != "":
                #        print("ddddd")
                commonStr = strDeleted

                os.chdir(oriCurDir)
                if not os.path.isdir(newDirNaem):
                        os.mkdir(newDirNaem)
                newFileName = newDirNaem + '/' + fileName.replace(".asp.htm", ".htm")
                fileNew = open(newFileName, 'w')
                fileNew.write(contentStr)
        os.chdir(oriCurDir)
        #fileNew = open(newDirNaem + 'chrX_common.html', 'w')
        #fileNew.write(commonStr)

  

def processADir_2(oriDirName, newDirNaem):
    if not os.path.isdir(oriDirName):
            print("error ./css is not a dir")
            return
    cssDir = os.listdir(oriDirName)
    commonStr = ""
    for fileName in cssDir:
        fileNameL = oriDirName + '/' + fileName
        if not os.path.isfile(fileNameL):
                print("error :" + fileNameL +": is not a file")
                
        curfile = open(fileNameL, 'r')
        try:
            contentStr = curfile.read()
        except UnicodeDecodeError as e:
                print(e + "****" + fileNameL)
        
        if contentStr.find('<script src="../chrX.js"></script>') == -1:
            print("no found in :" + fileNameL)
        curfile.close()
'''
        contentStr = contentStr.replace("框模型", "盒模型")
        contentStr = contentStr.replace("/css/", "/cssref/")
        #contentStr = contentStr.replace('href="pr_', 'href="../cssref/pr_')
        contentStr = contentStr.replace('<meta name="author" content="w3school.com.cn" />', '')
        #contentStr = contenStrDelAHtmlTagtStr.replace('http://w3school.com.cn/', '/chrX/nofile/123')
        

        w3StrIndex = contentStr.find('w3school')
        if w3StrIndex != -1:
                print('w3StrIndex:' + str(w3StrIndex))
        contentStr = deleteAndReturn(contentStr, '<div id="code">')[1]
        
        contentStr = '<iframe id="tiyiframe_' + strForName + '" style="visibility:hidden">\n' + contentStr + '\n</iframe>\n\n'

        contentStr = contentStr.replace('<!DOCTYPE html>', '')
        contentStr = contentStr.replace('<html>', '')
        contentStr = contentStr.replace('<html lang="zh-cn">', '')
        contentStr = contentStr.replace('</html>', '')
        contentStr = contentStr.replace('<li><a href="index.asp.htm" tppabs="http://w3school.com.cn/css/index.asp" title="CSS 教程">CSS 教程</a></li>\n', '')
        contentStr = contentStr.replace('<p><a href="../tiy/', '<p class="tiyClassInP" style="display:none"><a href="../tiy/t.asp')#('<p><a href="../tiy/[^">]*" >亲自试一试</a></p>')
        contentStr = contentStr.replace('<p>如需查看上例的效果，可以<a href="../tiy/', '<p class="tiyClassInP" style="display:none">如需查看上例的效果，可以<a href="../tiy/t.asp')
        contentStr = contentStr.replace('<div class="example">', '<div class="example" style="display:none">')
'''

'''
        contentStr = StrDelAHtmlTag(contentStr, '<div id="maincontent">', fileName)[0]
        contentStr = '<link rel="stylesheet" type="text/css" href="../c3.css" />\n\n<body class="html">\n<div id="wrapper">\n' + contentStr + '\n</div>\n<script src="../chrX.js"></script>'

        contentStr = StrDelAHtmlTag(contentStr, '<div id="tpn">', fileName)[1]
        contentStr = StrDelAHtmlTag(contentStr, '<div id="bpn">', fileName)[1]
        contentStr = contentStr.replace(".asp.htm", ".htm")

        def sssfun(matchobj):
            return '<a href="javascript:tiy.run(\'' + matchobj.group(1).replace('.htm', '') + '\')"'
        contentStr = re.sub('<a href="../tiy/[^=]+=([^"]+)"', sssfun, contentStr)
        

        #contentStr = StrDelAHtmlTag(contentStr, '<h2>浏览器支持</h2>', fileName)[1]
        
        contentStr = contentStr.replace('http://www.w3school.com.cn/', '/chrX/nofile/123')
        contentStr = contentStr.replace('\n\n文件并未加载在此文档，因为 它的域或路径超过开始网址中设置的范围。  \n\n你要从服务器上打开它吗？', '')
        reg = re.compile('\s?tppabs="http://[^"]+"\s?')
        contentStr = reg.sub(' ', contentStr)
        reg =  re.compile('\s?\n\s*\n\s*\n')
        contentStr = reg.sub('\n\n', contentStr)


        if not os.path.isdir(newDirNaem):
                os.mkdir(newDirNaem)
        newFileName = newDirNaem + '/' + fileName.replace(".asp.htm", ".htm")
        #newFileName = newDirNaem + '/tiy_' + strForName[: strForName.find("_")] + '.html'
        #print(newFileName)
        fileNew = open(newFileName, 'w')
        fileNew.write(contentStr)
        fileNew.close()
'''




#processADir('', '')
processADir_2('./css', './sql0')
