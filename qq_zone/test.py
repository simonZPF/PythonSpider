# -*-coding:utf8 -*-
import requests
import json
import re
head={"User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.12150.8 Safari/537.36",
      "Cookie":"__Q_w_s_hat_seed=1; eas_sid=K164w5S706j2f5i9A9c7X1h0d6; pgv_pvi=7693863936; o_cookie=316829772; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s__appDataSeed=1; cpu_performance_v8=32; RK=fBfSVQjHQd; ptui_loginuin=2928998636; pgv_pvid=3527290265; QZ_FE_WEBP_SUPPORT=1; pgv_info=ssid=s6400846887; ptisp=edu; ptcz=0caeffdf1124c092ab32f446b0dcfdb85d206e1d694546d18caeab4fbcb795ea; pt2gguin=o0316829772; uin=o0316829772; skey=@hhEMnST9C; p_uin=o0316829772; p_skey=QL1e9y0aL-jb*Ox7DGI488qYsSnJt4snOLZeuJ4Txw8_; pt4_token=jvUhwRn0EXJ3Y5oUE*zPsdqTJCljdKk-rwH5HEPE2*o_; Loading=Yes; _5t_trace_sid=1cdcdbdf93808872c48c23c5d3ab8d9d; _5t_trace_tms=1",
      "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      "Connection":"keep-alive"}

likeurl = "http://users.qzone.qq.com/cgi-bin/likes/get_like_list_app?uin=316829772&unikey=http%3A%2F%2Fuser.qzone.qq.com%2F316829772%2Fmood%2F{}.1&begin_uin=0&query_count=60&if_first_page=1&g_tk=1582597240"
html=requests.get(likeurl.format('4c70e212f8f4285754fe0500'),headers=head)
print html
content=re.findall('_Callback\((.*?)\);',html.content,re.S)[0]
info = json.loads(content)
data=info['data']
likenumber=0
like_nickdict={}
like_genderdict={}
like_constellationdict={}

def addTodict(key,dict):
        if key in dict:
            dict[key]+=1
        else:
            dict[key]=1

for each in data['like_uin_info']:
    gender=each['gender']
    constellation=each['constellation']
    nick=each['nick']
    addTodict(gender,like_genderdict)
    addTodict(constellation,like_constellationdict)
    addTodict(nick,like_nickdict)
print like_nickdict