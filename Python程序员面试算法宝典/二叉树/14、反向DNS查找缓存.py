"""
IP  ---->  域名

1、将IP地址添加到缓存中的URL映射
2、根据给定IP地址查找对应的URL

方法一：
    字典存储
方法二：
    Trie树
    1、使用Trie树，在最欢的情况下的时间复杂度为O(1),而哈希方法在平均情况下的时间复杂度为O(1)
    2、Trie树可以实现前缀搜索(对于有相同前缀的IP地址，可以寻找所有的URL)
        当然，由于树这种数据结构本身的特性，所以使用树结构的一个最大的缺点就是需要耗费更多的内存，但是对于本题而言，这却不是
        一个问题，因为Internet IP地址只包含有11个字母(0-9)。所以，本题实现的主要思路为：在Trie树中存储IP地址，而在最后一个结点中
        存储对应的域名。

只包含特定的11个字符（数字和.）
"""


# Trie树的结点
class TrieNode:
    def __init__(self):
        CHAR_COUNT = 11
        self.isLeaf = False
        self.url = None
        self.child = [None] * CHAR_COUNT


def getIndexFromChar(c):
    return 10 if c == '.' else (ord(c) - ord('0'))


def getCharFromIndex(i):
    return '.' if i == 10 else ('0' + str(i))


class DNSCache:
    def __init__(self):
        self.CHAR_COUNT = 11  # IP地址最多有11个不同的字符
        self.root = TrieNode()  # IP地址最大的长度

    def insert(self, ip, url):
        """
        ip地址的长度
        :param ip:      10.57.11.127
        :param url:     www.samsung.com
        :return:
        """
        lens = len(ip)
        pCrawl = self.root
        level = 0
        while level < lens:
            # 根据当前遍历到的IP中的字符,找出子结点的索引
            index = getIndexFromChar(ip[level])

            # 如果子结点不存在，则创建一个
            if pCrawl.child[index] is None:
                pCrawl.child[index] = TrieNode()

            # 移动到子结点
            pCrawl = pCrawl.child[index]
            # 在叶子结点中存储IP对应的URL
            pCrawl.isLeaf = True
            pCrawl.url = url
            level += 1

    # 通过IP地址找到对应的URL
    def searchDNSCache(self, ip):
        pCrawl = self.root
        lens = len(ip)
        # 遍历IP地址中所有的字符
        level = 0
        while level < lens:
            index = getIndexFromChar(ip[level])
            if pCrawl.child[index] is None:
                return None
            pCrawl = pCrawl.child[index]
            level += 1
        # 返回找到的URL
        if pCrawl is None and pCrawl.isLeaf:
            return pCrawl.url
        return None


if __name__ == '__main__':
    ipAdds = ['10.57.11.127', '121.57.61.129', '66.125.100.103']
    url = ['www.samsung.com', 'www.samsung.net', 'www.google.in']
    n = len(ipAdds)
    cache = DNSCache()
    for i in range(n):
        cache.insert(ipAdds[i], url[i])
        i += 1
    ip = '121.57.61.129'
    res_url = cache.searchDNSCache(ip)
    if res_url is not None:
        print('找到了IP对应的URL:\n' + ip + '----->' + res_url)
    else:
        print('没有找到对应的URL\n')
