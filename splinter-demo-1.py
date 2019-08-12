import time
# from splinter import Browser

from selenium import webdriver
# https://www.2cto.com/kf/201704/622848.html

def splinter(url):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    driver = webdriver.Chrome(chrome_options=options)

    # driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.switch_to.frame('x-URS-iframe')
    # 这里的不存在fill方法，但编译不报错，设置编译检查   TODO
    # driver.find_element_by_name('email').fill('yuan.zk')
    # driver.find_element_by_id('password').fill('123456')
    # TODO __setattr__()不能自动填充
    driver.find_element_by_name("email").__setattr__("value", "yuanzhikang")
    driver.find_element_by_name("password").__setattr__("value", "123456")
    time.sleep(5)
    driver.find_element_by_id('dologin').click()
    time.sleep(8)
    # driver.quit()

if __name__ == '__main__':
    websize3 ='http://www.126.com'
    splinter(websize3)

# 相关搜索：chromedriver操作

# <iframe src="myframetest.html" />
# 通常采用id和name就能够解决绝大多数问题。但有时候frame并无这两项属性，则可以用index和WebElement来定位：
#
# index从0开始，传入整型参数即判定为用index定位，传入str参数则判定为用id/name定位
# WebElement对象，即用find_element系列方法所取得的对象，我们可以用tag_name、xpath等来定位frame对象
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'myframe')]"))

# 从frame中切回主文档(switch_to.default_content())
# driver.switch_to.default_content()

# iframe嵌套
# <html>
#     <iframe id="frame1">
#         <iframe id="frame2" / >
#     </iframe>
# </html>

# driver.switch_to.frame("frame1")
# driver.switch_to.frame("frame2")
#
# driver.switch_to.parent_frame()  # 如果当前已是主文档，则无效果
#
# 综述，通常使用下面三个方法：
# driver.switch_to.frame(reference)
# driver.switch_to.parent_frame()
# driver.switch_to.default_content()

#
# 博客专栏
# Python Selenium自动化测试详解
# https://blog.csdn.net/column/details/12694.html





