from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['192.168.81.131'])


class Article(Document):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    body = Text(analyzer='snowball')
    tags = Keyword()
    published_from = Date()
    lines = Integer()

    class Index:
        name = 'blxog'
        settings = {
            "number_of_shards": 4,
        }

    def save(self, **kwargs):
        self.lines = len(self.body.split())
        return super(Article, self).save(**kwargs)

    def is_published(self):
        return datetime.now() >= self.published_from


# create the mappings in elasticsearch
Article.init()  # 创建映射关系，初始化索引库，以及type信息，一次性

# create and save and article  一条记录
article = Article(meta={'id': 422}, title='Hello world!', tags=['test'])
article.body = ''' looong text '''
article.published_from = datetime.now()
article.save()

article = Article.get(id=42)
print(article.is_published())

# Display cluster health
print(connections.get_connection().cluster.health())

"""
True
{
    'cluster_name': 'elasticsearch',
    'status': 'yellow', 
    'timed_out': False, 
    'number_of_nodes': 1, 
    'number_of_data_nodes': 1, 
    'active_primary_shards': 13, 
    'active_shards': 13, 
    'relocating_shards': 0, 
    'initializing_shards': 0, 
    'unassigned_shards': 13, 
    'delayed_unassigned_shards': 0, 
    'number_of_pending_tasks': 0, 
    'number_of_in_flight_fetch': 0, 
    'task_max_waiting_in_queue_millis': 0, 
    'active_shards_percent_as_number': 50.0
}

"""
