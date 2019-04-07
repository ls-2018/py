# from selenium import webdriver
# bro = webdriver.PhantomJS(executable_path=r"./phantomjs.exe")
# bro.get("https://www.baidu.com")
# bro.save_screenshot("1.png")
# text = bro.find_element_by_id("kw")
# text.send_keys("张三")
# bro.save_screenshot("2.png")
# bro.find_element_by_id("su").click()
# bro.save_screenshot("3.png")
# text.clear()
# bro.save_screenshot("4.png")
# text.send_keys("张三1")
# bro.save_screenshot("5.png")
# bro.find_element_by_id("su").click()
# bro.save_screenshot("6.png")
# bro.quit()
# D:\Python36\lib\site-packages\selenium\webdriver\phantomjs\webdriver.py:49: UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
#   warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 驱动路径
path = r'C:\Users\ZBLi\Desktop\1801\day05\ziliao\chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
# 上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)

browser.save_screenshot('baidu.png')
browser.quit()