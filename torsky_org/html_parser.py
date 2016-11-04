# coding:utf8
'''
Created on 2016年4月19日

@author: Administrator
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # index
        # <a href='details.php?fid=5556138729&fg=1' class='text6'>&nbsp;[BigNaturals] Stacy</a>
        links = soup.find_all('a',href=re.compile(r"details.php\?fid=\S+"))
        for link in links:
            new_url = link["href"]
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        #details.php  
        if "details.php" in page_url:
            links2 = soup.find_all('a',href=re.compile(r"http://xscreen\.allvie\.com/(view|image)\.php\?imgid=\w+"))
            for link2 in links2:
                new_url = link2["href"]
                new_urls.add(new_url)
        if  len(new_urls) == 0:
            print "len(new_urls) == 0"
            print ("page_url:%s" % page_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        # level:0
        '''
        links = soup.find_all('a',href=re.compile(r"details.php\?fid=\S+"))
        for link in links:
            res_data = {}
            href = link["href"]
            urlResult=urlparse.urlparse(href)
            urlParams=urlparse.parse_qs(urlResult.query,True)
            res_data['fid']=''.join(urlParams['fid'])
            res_data['title'] = link.get_text()
            res_data['url']=  urlparse.urljoin(page_url,href)     
            ls_data.append(res_data)
            '''
                
        #details.php  
        if "details.php" in page_url:
            tor_url = soup.find("input", {"name": "fileid"})['value']
            
            urlResult=urlparse.urlparse(page_url)
            urlParams=urlparse.parse_qs(urlResult.query,True)
            fid=''.join(urlParams['fid'])
            
            img_urls = set()
            links2 = soup.find_all('a',href=re.compile(r"http://xscreen\.allvie\.com/(view|image)\.php\?imgid=\w+"))
            for link2 in links2:
                new_url = link2["href"]
                img_urls.add(new_url)            
            
            res_data["fid"] = fid
            res_data["tor_url"] = tor_url
            res_data["img_urls"] = img_urls
        if "view.php" in page_url or "image.php" in page_url:
            img_node = soup.find("span",id="imagecode").find("img")
                        
            res_data["img_url"] = page_url
            res_data["img_src"] = urlparse.urljoin(page_url,img_node["src"])
        if len(res_data) == 0:
            print "len(res_data) == 0!"
            print ("page_url:%s" % page_url)
        return res_data
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        html_cont = html_cont.replace(';"">',';">')
        
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
    
    



