# sb = "人ABC们DEF"
#
#
# def to_unicode(string):
#     ret = ''
#     for v in string:
#         ret = ret + hex(ord(v)).upper().replace('0X', '\\u')
#
#     return ret
#
#
# demo = to_unicode(sb)
# print(demo)

# Unicode转中文
# python2：
s = '\u54c8\u54c8'
print(1, s.encode('unicode_escape'))
print(2, s.encode('utf8'))
# python3：
s = '\u54c8\u54c8'
print(3, s)

# 中文转unicode
# python2：(待验证)
# s='哈哈'
# ss = unicode(s, "utf-8")
# print(ss)
# python3：
s = '哈哈'
import json

ss = json.dumps(s)
print(4, ss)
print(5, '哈哈'.encode('utf8'))

print(u'\u4e00' <= '中' <= u'\u9fa5')
