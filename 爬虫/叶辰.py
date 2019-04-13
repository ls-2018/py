import requests
from bs4 import BeautifulSoup

response = requests.get(url='http://www.bjsxjy.com/199627.shtml')

soup = BeautifulSoup(response.text, features="html.parser")

soup = soup.find(name='div', attrs={'class': 'public_col_3'})
a_list = soup.find_all(name='a')
f = open('123.txt', 'w', encoding='utf-8')

for i in a_list:
    title = str(i.decode_contents()).encode('ISO-8859-1').decode('gbk')

    print(i.get('href'), '---', title)

    response_2 = requests.get(url=i.get('href'))
    soup_2 = BeautifulSoup(response_2.text, features="html.parser")
    div = soup_2.find(name='div', attrs={'class': 'public_ad_content'})
    text = str(div.get_text()).encode('ISO-8859-1').decode('gbk').replace(' ','')
    text = text.replace('牋牋','')
    f.write(title + '\n')
    f.write(text + '\n')
f.close()
