from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '15949600'
API_KEY = 'k9tDMxR017I5cNVDrx0XOBsM'
SECRET_KEY = 'i1WmYITKoFskWPp64Og55U7wqCaHxwGz'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# image = get_file_content('test.jpg')
# {'log_id': 2794194094609589127, 'words_result_num': 1, 'words_result': [{'words': '5739'}]}

""" 调用通用文字识别, 图片参数为本地图片 """
# res = client.basicGeneral(image)
# print(res)
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image, options)
#
# url = "http//www.x.com/sample.jpg"
#
""" 调用通用文字识别, 图片参数为远程url图片 """
# res = client.basicGeneralUrl(url='https://ps.ssl.qhimg.com/sdmt/432_162_100/t0171742c68d1bddc1f.webp')
# print(res)
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"

# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)
#

url = "https://so.gushiwen.org/RandCode.ashx?t=1554609824471?t=1554609825313?t=1554609826123?t=1554609828322?t=1554609829559"

""" 调用通用文字识别（含位置信息版）, 图片参数为远程url图片 """
res = client.generalUrl(url)

print(res)
