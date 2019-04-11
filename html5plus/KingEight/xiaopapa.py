import requests
from settings import MONGO

content_url = '/ertong/454529/7713571'
content_id = content_url.rsplit('/', 1)[1]
res = requests.get('https://m.ximalaya.com/tracks/%s.json' % (content_id))
content_info = res.json()

audio = requests.get(content_info.get('play_path'))
with open('123.mp3', 'wb') as f:
    f.write(audio.content)

img = requests.get(content_info.get('cover_url'))
with open('123.jpg', 'wb') as f:
    f.write(img.content)
title = content_info.get('title')
nickname = content_info.get('nickname')
album_title = content_info.get('album_title')
intro = content_info.get('intro')
play_count = content_info.get('play_count')

content = {
    'title': title,
    'nickname': nickname,
    'album_title': album_title,
    'intro': intro,
    'play_count': play_count,
    'audio': '123.mp3',
    'cover': '123.jpg'
}

MONGO.content.insert_one(content)
