#-*- coding:utf-8 -*-

import requests
from lxml import etree
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.11815.13 Safari/537.36",
         "Host":"trace.yto.net.cn:8022",
         "Referer":"http://www.yto.net.cn/gw/index/index.html",
         "Origin":"http://www.yto.net.cn"}
url="http://trace.yto.net.cn:8022/TraceSimple.aspx"
params = {'waybillNo':'881464403382458207', 'validateCode': '','jsessionId':''}
html=requests.post(url,data=params,headers=headers)
print html.text


