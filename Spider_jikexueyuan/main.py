#coding:utf-8
import requests
import re
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
course_url='http://www.jikexueyuan.com/course/?pageNum=2'
html=requests.get(course_url)
course=re.findall('<div class="lesson-infor" style="height: 88px;">(.*?)</div>',html.text,re.S)
for each in course:
    name=re.findall('<h2 class="lesson-info-h2">(.*?)</h2>',each,re.S)
    course_name=re.findall('">(.*?)</a>',name[0],re.S)
    introduce=re.findall('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>',each,re.S)
    times=re.findall('<i class="time-icon"></i><em>(.*?)</em>',each,re.S)
    grade=re.findall('<i class="xinhao-icon2"></i><em>(.*?)</em>',each,re.S)
    number=re.findall('<em class="learn-number">(.*>)</em>',each,re.S)
    print course_name[0]+introduce[0]+times[0]
