from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPagination(CursorPagination):
    # - 根据加密：http: // www.luffycity.com / api / v1 / student /?cursor = erd8
    cursor_query_param = 'cursor'  # 根据什么参数取数据?cursor=1
    ordering = '-created'
    page_size = 2


from rest_framework.views import APIView

# 'DEFAULT_PARSER_CLASSES': (
#     'rest_framework.parsers.JSONParser',
#     'rest_framework.parsers.FormParser',
#     'rest_framework.parsers.MultiPartParser'
# )

# models
# __all__ = ['tables1',]

# admin
# from . import models
# for tables in models.__all__:
#     admin.site.register(getattr(models,table))
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation

# biao1
# a= xxx()# 表的名字
# b=xxx()   # 内部实例
# c = GenericForeignKey('contenttype',b)
from rest_framework.views import APIView