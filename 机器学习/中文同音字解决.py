# 圆圆   媛媛

from pypinyin import lazy_pinyin,\
    TONE2,TONE,TONE3
# 模式一
a = lazy_pinyin('圆圆',style=TONE)
print(a)# ['yuán', 'yuán']

a = lazy_pinyin('媛媛',style=TONE)
print(a)# ['yuàn', 'yuàn']


# 模式二
a = lazy_pinyin('圆圆',style=TONE2)
print(a)# ['yua2n', 'yua2n']

a = lazy_pinyin('媛媛',style=TONE2)
print(a)# ['yua4n', 'yua4n']

# 模式三
a = lazy_pinyin('圆圆',style=TONE3)
print(a)# ['yuan2', 'yuan2']

a = lazy_pinyin('媛媛',style=TONE3)
print(a)# ['yuan4', 'yuan4']