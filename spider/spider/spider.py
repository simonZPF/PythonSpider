# -*- coding:utf8 -*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("gb18030")
type= sys.getfilesystemencoding()

html=requests.get('http://jp.tingroom.com/yuedu/yd300p',)
html.encoding='utf-8'
text=html.text
navMenu=re.findall('<div id="navMenu">(.*?)</div>',text,re.S)

nav=re.findall("'>(.*?)</a>",navMenu[0],re.S)
for each in nav:
    print each


