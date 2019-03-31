def generator_func():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3
    print('d')

g = generator_func()
ret1 = next(g)
print(ret1)
ret2 = next(g)
print(ret2)
ret3 = next(g)
print(ret3)
# 当函数中已经没有更多的yield时继续执行next(g)，遇到StopIteration

# send向生成器中发送数据，send的作用相当于next，只是在驱动生成器继续执行的同时还可以向生成器中传递参数