# -*- coding:utf -*-
import requests
from lxml import etree
import time
class Express(object):
    def __init__(self,start,end,weight,proxiesList=None):
        self.proxiesList=proxiesList
        self.proxies=None
        self.base_url="http://www.chakd.com/index.php?action=search" \
                 "&start=%s&end=%s&weight=%d" % (start,end,weight)
        self.curl="http://www.chakd.com/"
        self.nexturlbegin="http://www.chakd.com/index.php"
        self.url=self.base_url
        self.dictList=[]
        self.item=0
        self.spider()

    def spider(self):
        html=requests.get(self.url,proxies=self.proxies)
        html.encoding='gb2312'
        text=html.text
        selector=etree.HTML(text)
        start_place=selector.xpath('/html/body/div[3]/div/table[4]/tr/td[1]/div/a[1]/text()')
        start_place_url=selector.xpath('/html/body/div[3]/div/table[4]/tr/td[1]/div/a[1]/@href')
        end_place=selector.xpath('/html/body/div[3]/div/table[4]/tr/td[1]/div/a[2]/text()')
        end_place_url=selector.xpath('/html/body/div[3]/div/table[4]/tr/td[1]/div/a[2]/@href')
        price=selector.xpath('/html/body/div[3]/div/table[4]/tr/td[2]/div/text()')
        costtime=selector.xpath('/html/body/div[3]/div/table[4]/tr/td[3]/div/text()')
        isFreightcollect=selector.xpath('/html/body/div[3]/div/table[4]/tr/td[4]/div/text()')

        for i in range(len(start_place)):
            self.item+=1
            expressdict=dict(start=start_place[i],
                             startCompanyurl=self.curl+start_place_url[i],
                             end=end_place[i],
                             endCompanyurl=self.curl+end_place_url[i],
                             price=price[i],
                             time=costtime[i],
                             isFreightcollect=isFreightcollect[i])
            self.dictList.append(expressdict)
        try:
            next_page=selector.xpath('/html/body/div[3]/div/table[5]/tr/td/div/a[2]/@href')
            next_content=selector.xpath('/html/body/div[3]/div/table[5]/tr/td/div/a[2]/text()')
        except:
            next_page=None
        if next_page and next_content[0]==u'下一页':
            if self.proxiesList:
                for proxy in self.proxiesList:
                    proxy="http://"+proxy
                    self.proxies={"http":proxy}
                    try:
                        self.url=self.nexturlbegin+next_page[0]
                        self.spider()
                        break
                    except:
                        print "fail"
            else:
                try:
                    self.url=self.nexturlbegin+next_page[0]
                    self.spider()
                except:
                    print "fail"


if __name__ =="__main__":
    e=Express('%B3%C9%B6%BC','%C9%F2%D1%F4',2)
    for expressdict in e.dictList:
        for key,value in expressdict.iteritems():
            print key+u" "+value
        print
    print e.item

