from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

res = EC.title_contains('百度一下') # 填入预期包含的字符
print(res)

