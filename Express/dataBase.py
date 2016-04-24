#-*- coding:utf-8 -*-

from express import Express
import pymongo
connection = pymongo.MongoClient()
tdb = connection.demo

expresses=Express('%B3%C9%B6%BC','%C9%F2%D1%F4',2)
post_info = tdb.test
print expresses.dictList
for each in expresses.dictList:
    print each
    post_info.insert(each)