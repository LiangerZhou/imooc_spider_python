# coding:utf8
'''
Created on 2016年4月19日

@author: Administrator
'''
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print '获取所有链接'
links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()
    
print '获取lacie的连接'
link_node = soup.find("a", href="http://example.com/elsie")
print link_node.name,link_node['href'],link_node.get_text()    

print "正则表达式"
link_node = soup.find("a", href=re.compile(r"ill"))
print link_node.name,link_node['href'],link_node.get_text() 

print 'test'
'''
html_part = "<a href='details.php?fid=5556138729&fg=1' class='text6'>&nbsp;[BigNaturals] Stacy</a>"
soup = BeautifulSoup(html_part,'html.parser',from_encoding='utf-8')
link_node = soup.find("a", href=re.compile(r"details.php\?fid=\S+"))
print link_node
'''
html_part = '<a target=_blank class=imglink href="http://xscreen.allvie.com/image.php?imgid=krIwBeHiBvpB" rel="nofollow">http://xscreen.allvie.com/image.php?imgid=krIwBeHiBvpB</a><br />';
soup = BeautifulSoup(html_part,'html.parser',from_encoding='utf-8')
links2 = soup.find_all('a',href=re.compile(r"http://xscreen\.allvie\.com/(view|image)\.php\?imgid=\w+"))
print links2