# coding:utf8
'''
Created on 2016年4月19日

@author: Administrator
'''
import os
import urllib2
import datetime


class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return
        if len(data) == 0:
            return
        self.datas.append(data)   
    
    def output_html(self):
        DATE = datetime.datetime.now()
        date_str = DATE.strftime('%Y-%m-%d')
        fout = open('output_%s.html' % date_str,'w')
        
        fout.write('<html>\r\n')
        fout.write('<meta charset="UTF-8">\r\n')
        fout.write("<body>\r\n")
        fout.write("<table border=1>\r\n")
        print self.datas
        for data in self.datas:
            if 'fid' in data:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['fid'])
                fout.write("<td>%s</td>" % data['tor_url'])
                fout.write("<td>%s</td>" % data['img_urls'])                
                fout.write("</tr>")
            
        
        for data in self.datas:
            if 'img_src' in data:
                fout.write("<tr>")
                fout.write("<td>&nbsp;&nbsp;</td>")
                fout.write("<td>%s</td>" % data['img_url'])
                fout.write("<td>%s</td>" % data['img_src'])                
                fout.write("</tr>")
            
                
        fout.write("<table>")
        fout.write("<body>")
        fout.write('<html>')
        
        
    def output_imgs(self):
        for data in self.datas:
            if 'img_src' in data:
                img_url = data["img_src"]
                img_path = img_url.replace("http://",'D:/')
                img_dir = os.path.dirname(img_path)
                if os.path.exists(img_dir) == False:
                    os.makedirs(img_dir)
                f = open(img_path,'w')
                req = urllib2.urlopen(img_url)
                buf = req.read()
                f.write(buf)
                f.close()                



