# -*-coding:utf-8-*-

import urllib.request


TargetUrl = "http://www.szairport.com/szairport/hbxx/hbxx.shtml"


def VisitWeb():
    resp = urllib.request.urlopen(TargetUrl)
    html = resp.read()
    print(html)


if __name__ == '__main__':
    print("--------------hello python--------------")
    VisitWeb()

































