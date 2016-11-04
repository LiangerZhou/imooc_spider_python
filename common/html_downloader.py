# coding:utf8
'''
Created on 2016年4月19日

@author: Administrator
'''
import urllib2
import datetime
import os


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        
        return response.read()
    
    
    def toFile(self,page_url,html_cont):
        date_now = datetime.datetime.now()
        dir_date = date_now.strftime('%Y-%m-%d')
        file_url = page_url.replace("http://","D:/" + dir_date +"/") 
        dir_base = os.path.dirname(file_url)
        if os.path.exists(dir_base) == False:
            os.makedirs(dir_base) 
               
        


