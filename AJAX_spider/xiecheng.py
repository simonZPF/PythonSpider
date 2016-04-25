# -*-coding:utf8 -*-
import requests
import json
import re
proxy = {'http': 'http://182.126.236.162:9999'}
head={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.11815.13 Safari/537.36",
          "Referer":"http://flights.ctrip.com/booking/BJS-SHA-day-1.html",
          "Host":"flights.ctrip.com",
           "Connection":"keep-alive",
      "Accept-Encoding":"gzip, deflate",
      "Accept":"*/*",
      "Cache-Control":"private",
      "Cookie":'_abtest_userid=6faa3b86-cc67-48fb-86b4-78fa72c0ad2c; ASP.NET_SessionSvc=MTAuOC45Mi4xNzJ8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTQ0OTEzNzUxNzEwMg; adscityen=Shenyang; appFloatCnt=4; manualclose=1; __utma=13090024.949107489.1419085219.1461524930.1461524930.1; __utmc=13090024; __utmz=13090024.1461524930.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; DomesticUserHostCity=SHE|%c9%f2%d1%f4; _5t_trace_sid=5b173bfc8fbc44370e14ed647abba7bd; _5t_trace_tms=1; _gat=1; Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; traceExt=campaign=CHNbaidu81&adid=index; FD_SearchHistorty={"type":"S","data":"S%24%u5317%u4EAC%28BJS%29%24BJS%242016-04-30%24%u4E0A%u6D77%28SHA%29%24SHA%24%24%24"}; _bfa=1.1419085218543.2j1389.1.1461528574722.1461531244470.8.82; _bfs=1.7; _ga=GA1.2.949107489.1419085219; __zpspc=9.15.1461532825.1461532833.2%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%25E6%2597%2585%25E8%25A1%258C%25E7%25BD%2591%7C%23; _jzqco=%7C%7C%7C%7C1461519240364%7C1.821600962.1460829456084.1461532825848.1461532833396.1461532825848.1461532833396.undefined.0.0.37.37; _bfi=p1%3D101027%26p2%3D100101991%26v1%3D82%26v2%3D81'}
def findprice(start,end,time):
    if start==end:
        return [0]
    url="http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?" \
        "DCity1=%s&ACity1=%s&SearchType=S&DDate1=2016-%s" % (start,end,time)
    html=requests.get(url,headers=head,proxies=proxy)
    print html.content
    info = json.loads(html.content,encoding="gb2312")
    #print info
    priceList=[]
    fis=info['fis']
    for fly in fis:
        #print fly['fn']
        #print u'dt:  '+fly['dt'],u'at:  '+fly['at']
        for each in fly['scs']:
            #print each['p']
            priceList.append(int(each['p']))
    return sorted(priceList)[:3]
def getCode():
    # url="http://webresource.c-ctrip.com/code/cquery/resource/address/flight/flight_new_poi_gb2312.js"
    # head={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.11815.13 Safari/537.36",
    #       "Referer":"http://flights.ctrip.com/",
    #       "Host":"webresource.c-ctrip.com",
    #       "Cookie":"_5t_trace_sid=7e0bc0ad89431c5512c03a3361220514; _5t_trace_tms=1"}
    # html=requests.get(url,headers=head)
    # html.encoding='gb2312'
    with open("code.txt",'r')as f:
        text=f.read()
        # print text
        codeList=re.findall(r'\)(.*?)"}',text)
        codelist=[]
        for each in codeList:
            if(len(each[2:])==3):
            	codelist.append(each[2:])
        return codelist

def Allprice(place1,place2):
    codelist=getCode()
    placeDict={}
    with open("price.txt",'w')as f:
        for place in codelist:
            print place
            try:
                placeDict[place]=[x+y for x in findprice(place1,place,"4-30")
                                  for y in findprice(place2,place,"4-30")]
                i=findprice(place1,place,"4-30")
                print i
                f.write(str(i)+u'\n')
            except:
                pass
        # for each in placeDict:
        #     print each
        f.write(str(placeDict))

Allprice("SHE","CTU")
# getCode()
#print findprice("BJS","SHA","4-30")