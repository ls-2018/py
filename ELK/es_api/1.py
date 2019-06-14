from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch(hosts={"host": "192.168.81.131", "port": 9200})

s = Search(using=client, index='test').filter('name', catrgory='search').query('match', 'jack')
# s.aggs.bucket()
response = s.execute()
for hit in response:
    print(hit.meta.score, hit.title)
