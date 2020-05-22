from peewee_async import Manager
from tornado import web, ioloop

from LehuForum.settings import settings, database
from LehuForum.urls import urlpatterns

if __name__ == "__main__":
    # 集成json到wtforms
    import wtforms_json

    wtforms_json.init()

    app = web.Application(urlpatterns, debug=True, **settings)
    app.listen(9001)

    objects = Manager(database)
    # No need for sync anymore!
    database.set_allow_sync(False)
    app.objects = objects

    ioloop.IOLoop.current().start()
