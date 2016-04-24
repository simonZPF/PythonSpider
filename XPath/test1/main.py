# coding: utf-8
import requests
import sys
from lxml import etree
reload(sys)
sys.setdefaultencoding("utf-8")
html='''
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>lala</title>

</head>
<body>
 <form id="form1">
     <div id="aa">
        i
       <span for="name">
            love
            <div>
                 python
            </div>
            hehe
       </span>
       da
     </div>
</body>
</html>

'''
# course_url='http://www.jikexueyuan.com/course/?pageNum=2'
# html=requests.get(course_url)
# selector=etree.HTML(html.text)
# content=selector.xpath('//*[@id="2509"]/div[2]/h2/a/text()')
# print content[0]

# content=selector.xpath('//li[starts-with(@id,"2")]/div[2]/h2/a/text()')
# for each in content:
#     print each
selector=etree.HTML(html)
content=selector.xpath('//div[@id="aa"]')[0]
info=content.xpath('string(.)')
content_2=info.replace('\n','').replace(' ','')
print content_2