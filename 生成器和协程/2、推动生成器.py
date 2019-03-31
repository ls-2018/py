# 使用next函数从生成器中取值



def generator_from():
    print('a')
    yield 1

g= generator_from()
ret = next(g)
print(ret)

# 每一次next可以让生成器中的代码从上一个位置开始执行到yield，并且yield都免的值返回函数外部。


