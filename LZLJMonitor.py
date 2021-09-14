# -*-coding:utf-8-*-

import urllib.request
from urllib.error import HTTPError

from bs4 import BeautifulSoup
import time
import re

# import itchat

# Twilio L2jSBAe77Bq37ybqp_-gqFScl1DE_BTbPqJoeyM5

TargetUrl = ["https://shop73558189.m.youzan.com/wscgoods/detail/1ygk4fmjv1fmt?sub_kdt_id=73366021&dc_ps=2852093617168930823.200001&&mark_id=999_reallog_mark_ad%253A999%257CWeiboADNatural"
             ,"http://adkx.net/wsez1"
             ,"https://shop73558189.m.youzan.com/wscgoods/detail/2ohxwwbwf53k512"
             ,"https://j.youzan.com/EMBBl2"
             ,"https://shop73558189.m.youzan.com/wscgoods/detail/2g1qsfu152xp1?alias=2g1qsfu152xp1&pageType=TRADE&shopAutoEnter=1&sf=wx_sm&is_share=1&share_cmpt=native_wechat&dc_ps=2852095266201383944.200001&from_uuid=dde59c16-c8b3-30f7-0d9e-838577b8706d"
             ,"https://shop73558189.m.youzan.com/wscgoods/detail/2xkfedqqrvrjp?alias=2xkfedqqrvrjp&pageType=TRADE"
             ,"http://adkx.net/wsez6"
             ,"http://adkx.net/wsez0"
             ,"http://adkx.net/wsezf"
             ]

Address = ["广西南宁", "广东佛山", "湖北武汉", "山东青岛", "福建泉州", "福建厦门", "江西南昌", "江苏盐城", "广东深圳"]

MonitorAddressCnt = 10

RegexStockNum = r'"stockNum":(\d+)'
RegexIsDisplay = r'"isDisplay":(\d+)'
RegexSoldStatus = r'"soldStatus":"(\D+?)"'  #SALE为正常状态， SOLD_OUT为抢完售空状态

def visitweb():
    i = 0
    while i < len(Address):
        try:
            resp = urllib.request.urlopen(TargetUrl[i])
        except HTTPError as err:
            print(err.reason)
            i = i + 1
            continue
        except:
            print("Can not open the URL")
            i = i + 1
            continue

        html = resp.read()
        #print(html)
        soup = BeautifulSoup(html, "html.parser")
        # print(soup)

        # result = soup.find(text=text)
        # print(result)
        isDisplay = re.findall(RegexIsDisplay, str(soup))
        count = re.findall(RegexStockNum, str(soup))
        soldStatus = re.findall(RegexSoldStatus, str(soup))
        #print(count)

        print(soldStatus + isDisplay + count)
        if len(isDisplay) != 0 and isDisplay[0] != '0'\
                and len(count)!=0 and count[0] != '0'\
                and soldStatus[0] == "SALE":
            print(Address[i] + "有货啦， 数量为:" + count[0])
        # else:
            # print(Address[i] + "无货")

        i = i+1


def sendWechatMessage():
    # itchat.login()
    # itchat.send(u'你好，文件传输助手', 'filehelper')
    print("--------------sendWechatMessage--------------")


if __name__ == '__main__':
    print("--------------hello python--------------")
    while (1):
        print(time.strftime('%Y-%m-%d %H:%M:%S'), "1573监控。。。")
        visitweb()
        time.sleep(30)
