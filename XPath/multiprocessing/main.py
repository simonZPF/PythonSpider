import requests
import time
from multiprocessing.dummy import Pool
def geturl(url):
    html=requests.get(url)

urls=[]
for i in range(21):
    newpage = 'http://tieba.baidu.com/f?kw=%E9%AD%85%E6%97%8F&ie=utf-8&pn='+str(i*50)
    urls.append(newpage)
# time1=time.time()
# for each in url:
#     print each
#     geturl(each)
# time2=time.time()
# print time2-time1
pool=Pool(16)
time3=time.time()
result=pool.map(geturl,urls)
pool.close()
pool.join()
time4=time.time()
print time4-time3
