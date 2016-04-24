# -*- coding: utf-8 -*-

import requests
from lxml import etree
from multiprocessing.dummy import Pool

class proxyIP():
    def __init__(self,page=1):
        self.ipList=[]
        self.canUseList=[]
        self.page=page
        self.url = 'http://lwons.com/wx'
        self.run()

    def get_ip(self,page="1"):
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.11815.13 Safari/537.36"}
        html=requests.get("http://www.xicidaili.com/nt/"+page,headers=headers)
        text=html.text
        selector=etree.HTML(text)
        ip=selector.xpath("//*[@id='ip_list']/tr/td[3]/text()")
        host=selector.xpath('//*[@id="ip_list"]/tr/td[4]/text()')
        for i in range(len(ip)):
            st=str(ip[i])+u':'+str(host[i])
            self.ipList.append(st)
    def get_valid_proxies(self,p):
        proxy = {'http': 'http://' + p}
        try:
            r = requests.get(self.url, proxies=proxy)
            if r.text == 'default':
                self.canUseList.append(p)
                print 'success: ',p
        except Exception, e:
            print 'error: ', p

    def run(self):
        for i in range(self.page):
            self.get_ip(str(i+1))
        print len(self.ipList)
        pool=Pool(16)
        pool.map(self.get_valid_proxies,self.ipList)
        pool.close()
        pool.join()

if __name__ == '__main__':
    e=proxyIP()
    print len(e.canUseList)
