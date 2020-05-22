import peewee
import peewee_async
from app.conf.settings import app_settings
from app.conf import const

default_configs = app_settings[const.DB_CONFIG_ITEM][const.DEFAULT_DB_KEY]

database = peewee_async.MySQLDatabase(
    default_configs.get(const.DBNAME_KEY),
    user=default_configs.get(const.DBUSER_KEY),
    host=default_configs.get(const.DBHOST_KEY),
    port=default_configs.get(const.DBPORT_KEY),
    password=default_configs.get(const.DBPWD_KEY),
)
objects = peewee_async.Manager(database)
objects.database.set_allow_sync(False)


class TestNameModel(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = database
        table_name="xxxx"

    def __str__(self):
        return self.name


def init_table():
    # Clean up, can do it sync again:
    with objects.allow_sync():
        database.create_tables([TestNameModel], safe=True)  # safe=True 表存在的情况下,不会报错
    # TestNameModel.get_or_create(id=1, defaults={'name': "TestNameModel id=123"})
    # TestNameModel.get_or_create(id=3, defaults={'name': "TestNameModel id=3"})

# init_table()
