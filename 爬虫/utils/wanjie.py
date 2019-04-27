from urllib import request
import os
from selenium import webdriver
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPoll

chorme_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chorme_opt.add_experimental_option("prefs", prefs)
# bro = webdriver.Chrome(executable_path=r"./chromedriver.exe")
bro = webdriver.Chrome(executable_path=r"./chromedriver.exe", chrome_options=chorme_opt)
bro.get("http://www.gugu5.com/o/wanjiexianzong/")

a_list = bro.find_elements_by_xpath('//*[@id="play_0"]/ul/li/a')
pre_link = []
for a in a_list:
    href = a.get_attribute('href')
    title = a.get_attribute('title')
    pre_link.append((href, title))


def _get_img_1():
    for href, title in pre_link:
        if os.path.exists(f"./wanjie/{title}"):
            pass
        else:
            os.mkdir(f'./wanjie/{title}')
        bro.get(href)
        num = len(bro.find_elements_by_xpath('//*[@id="qTcms_select_i2"]/option '))
        for i in range(1, num + 1):
            src = bro.find_element_by_xpath('//*[@id="qTcms_pic"]').get_attribute('src')
            _get_img_2(title, src, i)
            btn = bro.find_element_by_xpath('//*[@id="qTcms_pic"]')
            btn.click()


# /html/body/div[8]/select/option[1]
def _get_img_2(title, src, num):
    print(title, num, src)
    request.urlretrieve(src, f'./wanjie/{title}/{num}.png')


if __name__ == '__main__':
    _get_img_1()

    # pool = ProcessPoll(3)  # 线程

    # pool.map(_get_img_1, pre_link)
    # pool.close()
    # pool.join()
    # print('---')
    # pool2 = ThreadPool(16)  # 线程
    # pool2.map(_get_img_2, img_link)
    # pool2.close()
    # pool2.join()
