# -*- coding: utf-8 -*-

import requests
from lxml import etree
from multiprocessing.dummy import Pool
import time
ipList=[]
canUseList=[]
url = 'http://lwons.com/wx'
def get_ip(page="1"):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.11815.13 Safari/537.36"}
    html=requests.get("http://www.xicidaili.com/nt/"+page,headers=headers)
    text=html.text
    selector=etree.HTML(text)
    ip=selector.xpath("//*[@id='ip_list']/tr/td[3]/text()")
    host=selector.xpath('//*[@id="ip_list"]/tr/td[4]/text()')
    for i in range(len(ip)):
        st=str(ip[i])+u':'+str(host[i])
        ipList.append(st)
def get_valid_proxies(p):
    proxy = {'http': 'http://' + p}
    try:
        r = requests.get(url, proxies=proxy)
        if r.text == 'default':
            canUseList.append(p)
            print 'success: ',p
    except Exception, e:
        print 'error: ', p

if __name__ == '__main__':
    for i in range(3):
        get_ip(str(i+1))
    print len(ipList)
    pool=Pool(16)
    time1=time.time()
    result=pool.map(get_valid_proxies,ipList)
    pool.close()
    pool.join()
    time2=time.time()
    print time2-time1
    print len(canUseList)