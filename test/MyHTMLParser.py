# coding:utf8
'''
Created on 2016年7月8日

@author: Administrator
'''
from HTMLParser import HTMLParser
import urllib,os
import sys
#reload(sys)
#sys.setdefaultencoding('gbk')

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links =  []
    def handle_starttag(self, tag, attrs):
#        print "Encountered the beginning of a %s tag" % tag
        if tag == 'img' or tag == "script":
            for (variable, value)  in attrs:
                if variable == "src" or variable == "href":
                    self.links.append(value)
        if tag == "link":
            dic = dict(attrs)
            if dic['rel']=="stylesheet":
                self.links.append(dic['href'])

def download(pagename,html_code,durl,links):
    if not os.path.exists(pagename+'_files\\'):
        os.mkdir(pagename+'_files\\')
    upurl = durl.rsplit('/',1)[0]
    for link in links:
        fname = link.split('/')[-1]
        fname = fname.split('?')[0]
        localpath = './%s%s' % (pagename+'_files/',fname)
        if link[0:3] == '../':
            downlink = link[3:]
            durl = upurl
        else:
            downlink = link

        try:
            urllib.urlretrieve(durl+'/'+downlink,localpath)
        except Exception,error:
            print 'download error:' , error
        else:
            print 'download '+fname
            html_code = html_code.replace(link,localpath)
    open(pagename+'.html','w').write(html_code)
    return True
if __name__ == "__main__":
    url = 'http://www.bathome.net/thread-30173-1-1.html'
    pagename = 'bathome'

    html_code = urllib.urlopen(url).read()
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    durl = url.rsplit('/',1)[0]
    print(durl)
    #download(pagename,html_code,durl,hp.links)
