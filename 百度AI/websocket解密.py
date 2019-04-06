# 由第一个字节与127得来，根据结果判断字符长度，解决粘包问题

# 0-125 字节长度

# 126 接下来2个字节为字符长度
print(2**64 -1)

# 127 取8个字节

str_byte= bytearray()
str_byte.append(1)
str_byte.append(1)
str_byte.append(1)
str_byte.append(1)

print(str_byte)