def throw_test():
    print('a')
    yield 1
    print('b')
    yield 2
g = throw_test()
next(g)
# g.throw(Exception,'xxxxxxxxx')  # 向生成器中抛一个异常
# throw和send、next相同，都是驱动生成器继续执行，只不过throw用来向生成器中抛一个异常
g.close()   # 关闭一个生成器
# next(g)