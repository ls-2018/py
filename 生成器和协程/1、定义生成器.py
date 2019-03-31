def generator_from():
    print('a')
    yield 1
g = generator_from()
print(g)
# 生成器 对象