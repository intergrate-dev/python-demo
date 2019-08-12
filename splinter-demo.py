import time

import ChromeDriver as ChromeDriver
from splinter import Browser

def splinter(url):
    browser = Browser()
    #login 126 email websize
    browser.visit(url)
    #wait web element loading
    time.sleep(5)
    #fill in account and password
    browser.find_by_id('idInput').fill('xxxxxx')
    browser.find_by_id('pwdInput').fill('xxxxx')
    #click the button of login
    browser.find_by_id('loginBtn').click()
    time.sleep(8)
    #close the window of brower
    browser.quit()

# https://www.2cto.com/kf/201704/622848.html

if __name__ == '__main__':
    websize3 ='http://www.126.com'
    splinter(websize3)
