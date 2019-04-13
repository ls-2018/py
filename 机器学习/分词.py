import jieba

jieba.add_word('我来到')# 在词库添加一个词,前提得符合逻辑
seg_list = jieba.cut('我来到北京清华大学', cut_all=True)  # 全模式
print(type(seg_list))
print(list(seg_list))

seg_list = jieba.cut('我来到北京清华大学', )  # 精确模式,cut_all默认False
print(type(seg_list))
print(list(seg_list))

seg_list = jieba.cut_for_search("我来到北京清华大学")  # 基于搜索引擎模式,更加准确,速度慢
print(type(seg_list))
print(list(seg_list))

#
# # 添加自定义字典
# '''
# 每一行分为三部分 ；
# ns 地点名词
# nz 其他专用名词
# a   形容词
# v   动词
# d   副词
# # dict.txt
# '''
# '''
# 乾清宫 5 ns
# 黄琉璃瓦 4
# 云计算 5
# 李小福 2 nr
# 凯特琳 2 nz
# '''
#
# jieba.load_userdict('dict.txt')
# text = '故宫的著名景点包括乾清宫、太和殿和黄琉璃瓦等'
# seg_list = jieba.cut(text, cut_all=False)
# print(type(seg_list))
# demo = list(seg_list)
#
# from collections import Counter
#
# demo_2 = Counter(demo)
# print(demo_2)  # Counter({1: 2, 2: 2, 3: 1, 4: 1})
# print(demo_2.most_common(1))  # 降序
#
# # 文本分类的关键词提取
#
# print('-------------------------------')
# '''当文本分类时，在构建VSM（空间向量模型）的过程中或者把文本转换成数字形式的计算中，需要运用到关键词提取的技术,jieba可以简便地提取'''
# import jieba
# import jieba.analyse
#
# jieba.load_userdict('dict.txt')
#
# seg_list = jieba.cut(text, cut_all=False)
#
# tags = jieba.analyse.extract_tags(sentence=text, topK=5, withWeight=False, allowPOS=())
# print('/'.join(tags))
# '''
# sentence    待提取的文本
# topK        返回几个TF/IDF权重最大的关键词
# withWeight  是否一并返回关键词权重值
# allowPOS    包含指定词性的词
# '''
#
# tags = jieba.analyse.extract_tags(sentence=text, topK=5, withWeight=UnicodeTranslateError, allowPOS=())
# print(tags)
#
#
#
#
#
# jieba.analyse.TFIDF(idf_path=None)  # 新建TF/IDF实例,idf_path为实例文件
# # 关键词提取所使用的逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径
# jieba.analyse.set_idf_path('fill_name') # fill_name 为自定义语料库的路径
# # 关键词所使用的停止词文本语料库可以切换成自定义语料库的路径
#
#
# '''
# TF/IDF的主要思想是：如果某个词或短语在一篇文章中出现的频率TF高,并且在其他文章中很少出现,则认为此词或者短语具有很好的类别区分能力,适合用来分类。
#
# '''