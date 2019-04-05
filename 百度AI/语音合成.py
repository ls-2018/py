from aip import AipSpeech

""" 你的 APPID AK SK """
# APP_ID = '你的 App ID'
# API_KEY = '你的 Api Key'
# SECRET_KEY = '你的 Secret Key'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

client.setConnectionTimeoutInMillis(1000)	# 建立连接的超时时间（单位：毫秒)
client.setSocketTimeoutInMillis(1000)	#通过打开的连接传输数据的超时时间（单位：毫秒）

result  = client.synthesis('你个大傻逼', 'zh', 1, {
    'vol': 0,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

# 参数	类型	描述	是否必须
# tex	String	合成的文本，使用UTF-8编码，
# 请注意文本长度必须小于1024字节	是
# cuid	String	用户唯一标识，用来区分用户，
# 填写机器 MAC 地址或 IMEI 码，长度为60以内	否
# spd	String	语速，取值0-9，默认为5中语速	否
# pit	String	音调，取值0-9，默认为5中语调	否
# vol	String	音量，取值0-15，默认为5中音量	否
# per	String	发音人选择, 0为女声，1为男声，
# 3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女	否




# // 成功返回二进制文件流
# // 失败返回
# {
#     "err_no":500,
#     "err_msg":"notsupport.",
#     "sn":"abcdefgh",
#     "idx":1
# }
# 错误码	含义
# 500	不支持的输入
# 501	输入参数不正确
# 502	token验证失败
# 503	合成后端错误