import jieba
from gensim import corpora
from gensim import models
from gensim import similarities

# from pymongo import MongoClient
# MONGO = MongoClient()['db']
# content = MONGO.stuinfo.find({})
# l1 = [con.get('title') for con in content]

l1 = ['播放光年之外', '野兽与美女', '播放美女与野兽', "我想听美女与野兽", '播放野兽与美女', '播放新球流浪']
a = "我想听美女与野兽"
# ------------>   匹配结果,与 这个稀疏矩阵相似度 有很大的关系
all_doc_list = []
for doc in l1:
    # doc_list = [word for word in jieba.cut_for_search(doc)]
    doc_list = [word for word in jieba.cut(doc)]
    all_doc_list.append(doc_list)

# print(all_doc_list)
doc_test_list = [word for word in jieba.cut(a)]
# doc_test_list = [word for word in jieba.cut_for_search(a)]
# print(doc_test_list)
# 制作语料库
dictionary = corpora.Dictionary(all_doc_list)  # 制作词袋
# 词袋的理解
# 词袋就是将很多很多的词,进行排列形成一个 词(key) 与一个 标志位(value) 的字典
# 例如: {'什么': 0, '你': 1, '名字': 2, '是': 3, '的': 4, '了': 5, '今年': 6, '几岁': 7, '多': 8, '有': 9, '胸多大': 10, '高': 11}
# 至于它是做什么用的,带着问题往下看

# print("token2id", dictionary.token2id)
# print("dictionary", dictionary, type(dictionary))

corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
# 语料库:
# 这里是将all_doc_list 中的每一个列表中的词语 与 dictionary 中的Key进行匹配
# 得到一个匹配后的结果,例如['你', '今年', '几岁', '了']
# 就可以得到 [(1, 1), (5, 1), (6, 1), (7, 1)]
# 1代表的的是 你 1代表出现一次, 5代表的是 了  1代表出现了一次, 以此类推 6 = 今年 , 7 = 几岁
# print("corpus", corpus, type(corpus))

# 将需要寻找相似度的分词列表 做成 语料库 doc_test_vec
doc_test_vec = dictionary.doc2bow(doc_test_list)
# print("doc_test_vec", doc_test_vec, type(doc_test_vec))

# 将corpus语料库(初识语料库) 使用Lsi模型进行训练
lsi = models.LsiModel(corpus)
# 这里的只是需要学习Lsi模型来了解的,这里不做阐述
# print("lsi", lsi, type(lsi))
# 语料库corpus的训练结果
# print("lsi[corpus]", lsi[corpus])
# 获得语料库doc_test_vec 在 语料库corpus的训练结果 中的 向量表示
# print("lsi[doc_test_vec]", lsi[doc_test_vec])

# 文本相似度
# 稀疏矩阵相似度 将 主 语料库corpus的训练结果 作为初始值
index = similarities.SparseMatrixSimilarity(lsi[corpus], num_features=len(dictionary.keys()))
# print("index", index, type(index))

# 边长\面积\形状...


# 将 语料库doc_test_vec 在 语料库corpus的训练结果 中的 向量表示 与 语料库corpus的 向量表示 做矩阵相似度计算
sim = index[lsi[doc_test_vec]]

# print("sim", sim, type(sim))

# 对下标和相似度结果进行一个排序,拿出相似度最高的结果
# cc = sorted(enumerate(sim), key=lambda item: item[1],reverse=True)
cc = sorted(enumerate(sim), key=lambda item: -item[1])
# print(cc)

text = l1[cc[0][0]]

jilv = cc[0][0]
if jilv > 0.7:
    print(a, text, '-----')
    'doing something other'

else:
    print('交给图灵处理')

all_doc_list = [['你', '的', '名字', '是', '什么'], ['你', '今年', '几岁', '了'], ['你', '有', '多', '高', '你', '胸多大'], ['你', '胸多大']]
doc_test_list = ['你', '今年', '多大', '了']
corpus = [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], [(1, 1), (5, 1), (6, 1), (7, 1)],
          [(1, 2), (8, 1), (9, 1), (10, 1), (11, 1)], [(1, 1), (10, 1)]]
doc_test_vec = [(1, 1), (5, 1), (6, 1)]
