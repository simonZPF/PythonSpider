# -*-coding:utf8 -*-
import requests
import json
import re
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# class Friend(dict):
#     def __init__(self,gender,constellation,is_qq_friend,nick):
#         self.infoDict={'gender':gender,
#                        'constellation':constellation,
#                        'is_qq_friend':is_qq_friend,
#                        'nick':nick,
#                        }
#
#
# class Talks(object):
#     def __init__(self,comments,likes,time):
#         self.comments=comments
#         self.likes=likes
#         self.time=time

class QQZoneSpider(object):
    def __init__(self):
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        self.url = "https://mobile.qzone.qq.com/get_feeds?" \
            "g_tk=1582597240&hostuin=316829772&res_type=2&res_attach=att%3" \
            "Dback%255Fserver%255Finfo%253Doffset%25253D{}%2525266&refresh_type=2" \
            "&format=json"
        self.likeurl = "http://users.edu.qzone.qq.com/cgi-bin/likes/get_like_list_app?uin=316829772&unikey=http%3A%2F%2Fuser.qzone.qq.com%2F316829772%2Fmood%2F{}.1%5E%7C%7C%5Ehttp%3A%2F%2Fuser.qzone.qq.com%2F316829772%2Fphoto%2FV12FMjWP1TP6qM%2FNDR0THDiEvb0KFfJw9YCcQEAAAAAAAA!%5E%7C%7C%5E0&begin_uin=0&query_count=60&if_first_page=1&g_tk=1582597240"
        self.head={"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.12150.8 Safari/537.36",
              "Cookie":"__Q_w_s_hat_seed=1; eas_sid=K164w5S706j2f5i9A9c7X1h0d6; pgv_pvi=7693863936; o_cookie=316829772; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s__appDataSeed=1; cpu_performance_v8=32; RK=fBfSVQjHQd; ptui_loginuin=2928998636; pgv_pvid=3527290265; QZ_FE_WEBP_SUPPORT=1; pgv_info=ssid=s6400846887; ptisp=edu; ptcz=0caeffdf1124c092ab32f446b0dcfdb85d206e1d694546d18caeab4fbcb795ea; pt2gguin=o0316829772; uin=o0316829772; skey=@hhEMnST9C; p_uin=o0316829772; p_skey=QL1e9y0aL-jb*Ox7DGI488qYsSnJt4snOLZeuJ4Txw8_; pt4_token=jvUhwRn0EXJ3Y5oUE*zPsdqTJCljdKk-rwH5HEPE2*o_; Loading=Yes; _5t_trace_sid=7232c76945e5a7b9c0139dc6b3b4399c"}
        self.head2={"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.12150.8 Safari/537.36",
              "Cookie":"__Q_w_s_hat_seed=1; eas_sid=K164w5S706j2f5i9A9c7X1h0d6; pgv_pvi=7693863936; o_cookie=316829772; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s__appDataSeed=1; cpu_performance_v8=32; RK=fBfSVQjHQd; ptui_loginuin=2928998636; pgv_pvid=3527290265; QZ_FE_WEBP_SUPPORT=1; pgv_info=ssid=s6400846887; ptisp=edu; ptcz=0caeffdf1124c092ab32f446b0dcfdb85d206e1d694546d18caeab4fbcb795ea; pt2gguin=o0316829772; uin=o0316829772; skey=@hhEMnST9C; p_uin=o0316829772; p_skey=QL1e9y0aL-jb*Ox7DGI488qYsSnJt4snOLZeuJ4Txw8_; pt4_token=jvUhwRn0EXJ3Y5oUE*zPsdqTJCljdKk-rwH5HEPE2*o_; Loading=Yes; _5t_trace_sid=1cdcdbdf93808872c48c23c5d3ab8d9d; _5t_trace_tms=1"}
        self.commentdict={}
        self.likenumber=0
        self.like_nickdict={}
        self.like_genderdict={}
        self.like_constellationdict={}
    def get(self,count):
        html=requests.get(self.url.format(count),headers=self.head)
        print html
        try:
            info = json.loads(html.content)
        except:
            return False
        if not info['data']:
            return False
        data = info['data']
        for i,talk in enumerate(data['vFeeds']):
            #print i
            time = talk['comm']['time']
            try:
                #print "comment people-------------"
                for commenter in talk['comment']['comments']:
                    commentname=commenter['user']['nickname']
                    self.addTodict(commentname,self.commentdict)
                #print '---------------------------'
            except:
                pass
            cellid=talk['id']['cellid']
            likehtml=requests.get(self.likeurl.format(cellid),headers=self.head2)
            try:
                content=re.findall('_Callback\((.*?)\);',likehtml.content,re.S)[0]
                info = json.loads(content)
                data=info['data']
                total_number=data['total_number']
                self.likenumber += total_number
                for each in data['like_uin_info']:
                    gender=each['gender']
                    constellation=each['constellation']
                    nick=each['nick']
                    self.addTodict(gender,self.like_genderdict)
                    self.addTodict(constellation,self.like_constellationdict)
                    self.addTodict(nick,self.like_nickdict)
                # print self.like_constellationdict
                # print self.like_genderdict
                # print self.like_nickdict
            except:
                print i," ------error--------------"


        return True

    def drawcomment(self):
        top10comment=sorted(self.commentdict.iteritems(),key=lambda a:a[1],reverse=True)[:10]
        timeslist=[]
        commentlist=[]
        for key,value in top10comment:
            commentlist.append(key)
            timeslist.append(int(value))

        self.drawZhu(commentlist,timeslist,'Comment',"comment",'times')
    def drawlike(self):
        top10likes=sorted(self.like_nickdict.iteritems(),key=lambda a:a[1],reverse=True)[:10]
        timeslist=[]
        commentlist=[]
        for key,value in top10likes:
            commentlist.append(key)
            timeslist.append(int(value))

        self.drawZhu(commentlist,timeslist,'Zan',"likes",'times')
    def drawgender(self):
        datalist=[]
        labelist=[]
        for key,value in self.like_genderdict.iteritems():
            if key!='':
                datalist.append(int(value))
                labelist.append(key)
        self.drawbin(datalist,labelist,"Gender",'gender')
    def drawconstellation(self):
        datalist=[]
        labelist=[]
        for key,value in self.like_constellationdict.iteritems():
            if key!='':
                datalist.append(int(value))
                labelist.append(key)
        self.drawbin(datalist,labelist,"Constellation",'constellation')


    def run(self):
        for i in range(120):
            try:
                print i
                self.get(str(i*10))
            except :
                print u"i= ",str(i),u"+++++++++++++++"

        #self.get(str(i*10))
        # for key,value in self.like_genderdict.iteritems():
        #     print key+u" : "+str(value)
        # for key,value in self.like_constellationdict.iteritems():
        #     print key+u" : "+str(value)
    def drawZhu(self,xaxisList,yaxisList,name,title=' ',ylabel=" ",N=10):
        ind = np.arange(N)  # the x locations for the groups
        width = 0.35
        fig,ax = plt.subplots()
        rects1 = ax.bar(ind,yaxisList, width, color='r')
        ax.set_ylabel('Times')
        ax.set_title(title)
        ax.set_xticks(ind+width)
        ax.set_xticklabels(xaxisList)
        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                        ha='center', va='bottom')
        autolabel(rects1)
        plt.savefig('%s.png' % name, format='png',dpi=200)
        plt.show()
    def drawbin(self,data,labels=[],title='',name=''):
        plt.figure(num=1, figsize=(15,15))
        plt.axes(aspect=1)
        plt.title(title, size=25)
        plt.pie(data,labels=labels,autopct='%0.2f%%', startangle=90,)
        plt.legend(loc='upper left')
        plt.savefig('%s.png' % name, format='png',dpi=200)
        plt.show()

    def addTodict(self,key,dict):
        if key in dict:
            dict[key]+=1
        else:
            dict[key]=1
q=QQZoneSpider()
q.run()
q.drawcomment()
q.drawconstellation()
q.drawlike()
q.drawgender()