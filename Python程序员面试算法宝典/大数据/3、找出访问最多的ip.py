"""



1、从访问记录中，遍历一次，获得IP将其写入新的文件。

    以IPV4为例，由于一个IP地址占用32位，因此最多会有4G种情况
    如果使用hash(IP)%1024会把海量的IP分别存储到1024个小文件中
    这样每个小文件最多包含4M个ip地址。如果使用2048个小文件，那么每个小文件最多包含2M个ip地址。



"""

from collections import Counter

demo_2 = Counter([1, 2, 3, 1,1,4, 2, 1])
print(demo_2)  # Counter({1: 2, 2: 2, 3: 1, 4: 1})
print(demo_2.most_common(3))  # 降序
