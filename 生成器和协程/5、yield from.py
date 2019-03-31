from itertools import chain

"""
    chain(*iterables) --> chain object
    
    Return a chain object whose .__next__() method returns elements from the
    first iterable until it is exhausted, then elements from the next
    iterable, until all of the iterables are exhausted.
"""
l = ['h', 'e', 'l']
dic = {'l': 'v1', 'o': 'v2'}
s = 'eva'


def yield_from_gen():
    yield from chain(l, dic, s)
    # yield 可以完成一个委派生成器的作用，在子生成器和调用者之间建立一个双向通道


for item in yield_from_gen():
    print(item, end='')
