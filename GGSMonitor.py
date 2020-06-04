# -*-coding:utf-8-*-

import urllib.request
from bs4 import BeautifulSoup
import time
import re
import itchat

# Twilio L2jSBAe77Bq37ybqp_-gqFScl1DE_BTbPqJoeyM5

TargetUrl = "https://gzgsv.xpshop.cn/products/product-1000233.html"

regex = r'"stock":"(\d+)"'

def visitweb():
    resp = urllib.request.urlopen(TargetUrl)
    html = resp.read()
    soup = BeautifulSoup(html, "html.parser")
    #print(soup)

    #result = soup.find(id = 'btnBuyNow')
    #print(result.text)
    count = re.findall(regex, str(soup))
    print(count)

    if count[0] == '0':
        print("贵高速目前茅台缺货...")
    else:
        print("贵高速茅台有货啦， 数量为:" + count[0])


def sendWechatMessage():
    itchat.login()
    itchat.send(u'你好，文件传输助手', 'filehelper')

if __name__ == '__main__':
    print("--------------hello python--------------")
    while(1):
        print(time.strftime('%Y-%m-%d %H:%M:%S'), "贵高速茅台监控。。。")
        visitweb()
        time.sleep(30)
