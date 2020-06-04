import sys
import io
import request
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    cookie_str = r'yourcookie'
    cookies = {}

    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    response = requests.get(url, headers=headers, cookies=cookies)  # 请求访问网站
    html = response.text  # 获取网页源码
    return html  # 返回网页源码


soup = BeautifulSoup(get_html(
    'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&type=10&isMul=1&isNew=1&lang=zh_CN&token=896485145'),
                     'lxml')  # 初始化BeautifulSoup库,并设置解析器
# print(get_html('https://www.jianshu.com/'))
print(soup.title)


