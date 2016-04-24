# -*-coding:utf8 -*-

import requests
import json
import re
url="http://comments.youku.com/comments/~ajax/vpcommentContent.html?__" \
    "ap=%7B%22videoid%22%3A%22XMTU0NTkxMTQ5Mg%3D%3D%22%2C%22sid%22%3A896591341%2C%22last_modify" \
    "%22%3A1461504343%2C%22showid%22%3A0%2C%22chkpgc%22%3A0%2C%22page%22%3A2%7D&" \
    "__ai=&__callback=displayComments"
head={"User-Agent":
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.11815.13 Safari/537.36"}
jscontent=requests.get(url,headers=head).content
contents = re.findall(r'<p id=\\\"\w*\\\">(.*?)<br \\/>',jscontent)
for content in  contents:
    print content.decode("unicode_escape")
# jsData = jsDict['data']
# comments = jsData["commentid"]
# for each in comments:
#     content = re.findall(r"<p>(.*?)</p>",each["content"])
#     for i in content:
#         print i