# -*- coding:utf-8 -*-
from multiprocessing.dummy import Pool
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
def getsource(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    name  = selector.xpath('//*[@id="j_p_postlist"]/div/div[1]/ul/li[3]/a/text()')
    time = selector.xpath('//*[@id="j_p_postlist"]/div/div[2]/div[2]/div[1]/div[2]/span[4]/text()')


urls=[]
for i in range(21):
    page='http://tieba.baidu.com/p/4348969988?pn='+str(i+1)
    urls.append(page)
getsource(urls[0])