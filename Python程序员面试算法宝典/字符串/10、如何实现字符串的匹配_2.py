"""
在方法一中,如果 P1P2...Pj = S(i-j)...S(i-1)  那么模式串的前j个字符已经和主串中i-j到i-1的字符进行了比较,
此时如果Pj!=Si,那么模式串需要退回到0,主串需要回退到i-j+1的位置重新开始下一次比较.

KMP算法,
如果Pj!=Si,那么不需要回退,即i保持不动,j也不用清零,而是向右滑动模式串,用Pk和Si继续匹配.这种方法的核心就是确定k的大小,显然k的值越大越好


P1P2...P(j-1) = S(i-j)...S(i-1) 如果主串第i个字符与模式串j匹配失败,

因此当模式串满足P0P1...P(k-1) = P(j-k)...P(j-1);那么只需要接着比较主串第i个字符和模式串第k个字符
为了在任何字符匹配失败的时候都能找到对应k的值,这里给出next数组的定义next[i]=m表示的意思为:P0P1...P(m-1) =P(i-m)...P(i-1)

计算方法如下
next[j]=-1  (当j==0时)
next[j]=max   (max{k | 1<k<j 且 P0P1...Pk = P(j-k-1)...P(j-1))
next[j]=0   其他情况

"""


def getNext(p, nexts):
    """"""
    i = 0
    j = -1
    nexts[0] = -1
    while i < len(p):
        if j == -1 or list(p)[i] == list(p)[j]:
            i += 1
            j += 1
            nexts[i] = j    # 指向相同的前一个
        else:
            j = nexts[j]    # 这里next[j]是之前匹配的上一个,


def match(s, p, nexts):
    # 检查参数的合理性,s>=p
    if s is None or p is None:
        print('参数不合理')
        return -1
    slen = len(s)
    plen = len(p)
    # p 肯定不是s的子串
    if slen < plen:
        return -1
    i = j = 0
    while i < slen and j < plen:
        print("i= ", i, ' j= ', j)
        if j == -1 or list(s)[i] == list(p)[j]:
            i += 1
            j += 1
        else:
            # 主串i不需要回溯,从next数组中找出需要比较的模式串的位置j
            j = nexts[j]

    if j >= plen:  # 匹配成功
        return i - plen

    return -1


if __name__ == '__main__':
    s = 'abababaabcbab'
    p = 'abaabc'
    lens = len(p)
    nexts = [0] * (lens + 1)
    getNext(p, nexts)
    print('nexts数组为:', nexts)
    print('匹配结尾为:', match(s, p, nexts))
