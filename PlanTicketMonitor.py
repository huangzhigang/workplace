# -*-coding:utf-8-*-

import urllib.request
from bs4 import BeautifulSoup
import re
import time

TargetUrl = "http://www.szairport.com/frontapp/HbxxServlet?iscookie=C"

testTxt = 'sdfsdf<tr class="even"><td rowspan="1" width="60">ZH9919</td><td rowspan="1" width="80">深圳 </td> </tr>'

regex = r'<td(.*)</td>'
regex2 = r"<td.*?>(.*?)</td>"

szhk = [[0]*10]*0


def getszhk(tr):
    for info in tr:
        text = str(info).replace('\n', '').replace('\t', '').replace('\r', '').replace('&gt; ','').replace(' ', '')
        td = re.findall(regex2, text)
        if td[1].find('深圳') != -1:
            global szhk
            existed = 0
            for item in szhk:
                if item[0] == td[0]:
                    existed = 1
                    if item[8] != td[8]:
                        print("深圳航班发生变化:", td[0], td[3], item[8], " -> ", td[8])
                        item[8] = td[8]
            if existed == 0 and len(td)==10:
                print("列表新增航班:", td)
                szhk.append(td)

def visitweb():
    resp = urllib.request.urlopen(TargetUrl)
    html = resp.read()
    soup = BeautifulSoup(html, "html.parser")

    tr = soup.select('.even')
    getszhk(tr)

    tr = soup.select('.odd')
    # print(tr)
    getszhk(tr)

    #print(szhk)


if __name__ == '__main__':
    print("--------------hello python--------------")
    while(1):
        print(time.strftime('%Y-%m-%d %H:%M:%S'), "航班查询执行。。。")
        visitweb()
        time.sleep(30)
