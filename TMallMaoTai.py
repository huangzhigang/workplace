import time
import datetime
import requests
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


#driver.find_element_by_id('J_CheckShop_s_725677994_1').click()
#driver.find_element_by_xpath('//*[@id="J_Item_1784751050782"]/ul/li[1]/div/div/div/label').click()

def getTMallTime():
    r1 = requests.get(url='http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp',
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'})
    x = eval(r1.text)
    timeNum = int(x['data']['t'])
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%H:%M:%S", timeArray)
    return otherStyleTime

def getSysTime():
    return datetime.datetime.now().strftime("%H:%M:%S:%f")[0:-3]

def submitOrder():
    try:
        print("结算提交时间:", datetime.datetime.now())
        #driver.find_element_by_xpath('//*[@id="J_Go"]').click()
        driver.find_element_by_id('J_Go').click()
        #driver.find_element_by_id('J_CheckBox_1784751050782').click()

        time.sleep(0.4)  #0.3 is ok is normal test.

        print("提交订单时间:", datetime.datetime.now())
        driver.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a[2]').click()
        print("提交订单结束:", datetime.datetime.now())
        time.sleep(0.5)

        driver.back()
        time.sleep(0.5)
    except:
        print("购买出现问题， 重新购买...")

if __name__ == '__main__':
    print("--------------hello python--------------")
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(options=chrome_options)
    print(driver.title)

    # 当前句柄
    current = driver.current_window_handle

    driver.get('https://cart.taobao.com/cart.htm?spm=a220o.7406545.a2226mz.12.758976dcZaU2Nj&from=btop')

    # 所有句柄
    heandles = driver.window_handles
    secondhand = heandles[-1]

    # 切回first
    driver.switch_to.window(current)

    #time.sleep(3)

    while(1):
        #print("天猫时间:", getTMallTime())
        print("系统时间:", getSysTime())
        if "19:59:59:700" <= getSysTime():
        #if "19:48:00" == getSysTime():
            submitOrder()
