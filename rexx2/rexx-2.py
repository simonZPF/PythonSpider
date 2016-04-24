# -*- coding:utf-8 -*-

import re
import requests
f = open('source.txt', 'r')
html = f.read()
f.close()
pic_url = re.findall('img src="(.*?)" class="lessonimg" ', html, re.S)
i = 0
for each in pic_url:
    print 'now downloading:' + each
    pic = requests.get(each)
    fp = open('pic\\'+str(i)+'.jpg', 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1

