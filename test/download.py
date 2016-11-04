# coding:utf8
'''
Created on 2016年7月8日

@author: Administrator
'''
import urllib2  
import os  
from bs4 import BeautifulSoup   
import re 
#import urlparse 
siteUrls = " "  
  
def getContent(url):  
    content = urllib2.urlopen(url).read()  
    content = writeCss(url,content) 
    content = writeImg(url,content)   
    fileName = "d:/"+ os.path.basename(url)  
    print fileName  
    f = file(fileName+".html",'w')  
    f.write(content)  
    f.close()  

def getHost(url):
    proto, rest = urllib2.splittype(url);
    host, rest = urllib2.splithost(rest)  
    return host  
def writeCss(url,content):  
    #dirPath = "d:/"+dirName 
    soup = BeautifulSoup(content, "html.parser")  
    csss = soup.findAll('link',attrs={'type':'text/css'})    
    for css in csss:  
        #cssnames = re.findall(r'.*/(.*)\.css',str(css))  
        cssurls = re.findall(r'.*href=\"([^\"]*)\"',str(css))     
        cssNewName = cssurls[0].replace("http://","d:/")  
        if(os.path.exists(cssNewName)):
            return content
        parentDir = os.path.dirname(cssNewName)
        print os.path.isdir(parentDir) 
        if not os.path.isdir(parentDir): 
            os.makedirs(parentDir)
        try:
            csscontent = urllib2.urlopen(cssurls[0]).read()  
        except Exception,error:
            print 'download error:' , error            
        cssfile = file(cssNewName,'w')  
        cssfile.write(csscontent)  
        cssfile.close()  
        content = content.replace(cssurls[0],cssNewName)
    return content  
  
def writeImg(url,content):  
    soup = BeautifulSoup(content,"html.parser")  
    imgs = soup.findAll('img')  
    for img in imgs:    
        imgUrls = re.findall(r'.*src=\"([^\"]*)\"',str(img))  
        #if(getHost(url) != getHost(imgUrls[0])):
        #    return content
        print imgUrls
        if(imgUrls[0].find('?') >= 0):
            continue
        imgNewName = imgUrls[0].replace("http://","d:/")
        print imgNewName
        if(os.path.exists(imgNewName)):
            return content
        parentDir = os.path.dirname(imgNewName)
        if not os.path.isdir(parentDir): 
            os.makedirs(parentDir)
        imgContent = urllib2.urlopen(imgUrls[0]).read()   
        imgfile = file(imgNewName,'w')  
        imgfile.write(imgContent)  
        imgfile.close()  
    return content  

url = "http://www.sina.com.cn"    
getContent(url)  
#print os.path.basename("d:/www.sina.com.cn?a=b")