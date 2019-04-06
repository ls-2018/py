from aip import AipSpeech, AipNlp

APP_ID = '15217111'
API_KEY = 'jE38mGiHGGe8LnmK2YdbGGoX'
SECRET_KEY = 'KaoFdHZoaUWQsmpRgIEgxIGhdkDbW2V4'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# client.setConnectionTimeoutInMillis()
# client.setSocketTimeoutInMillis()

result = client.synthesis('', 'zh', 1, {
    "per": 4,
    "pit": 8,
    "spd": 4,
    'vol': 5,
})


# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
print(result)
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

import os


# 读取文件
def get_file_content(filePath):
    os.system(f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()


# 识别本地文件
res = client.asr(get_file_content('xh.wma'), 'pcm', 16000, {
    'dev_pid': 1536,
})

Q = res.get("result")[0]
print(Q)

if nlp_client.simnet(Q, "你叫什么名字").get("score") >= 0.7:
    A = "我的名字叫金角大王八"
    result = client.synthesis(A, 'zh', 1, {
        "per": 4,
        "pit": 8,
        "spd": 4,
        'vol': 5,
    })
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)

    os.system('auido.mp3')

else:
    import goto_tuling

    A = goto_tuling.tl(Q, "jinwangba")
    result = client.synthesis(A, 'zh', 1, {
        "per": 4,
        "pit": 8,
        "spd": 4,
        'vol': 5,
    })
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)

    os.system('auido.mp3')