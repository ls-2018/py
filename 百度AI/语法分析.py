from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '15968480'
API_KEY = 'Vh6cS5dY6GjD6W14ymCMYh4U'
SECRET_KEY = '9PA8dVNb2zGsm3NIPlFuP1jGDBhkEwDt'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
text = "百度是一家高科技公司"

""" 调用词法分析 """
ret = client.lexer(text)
print(ret)