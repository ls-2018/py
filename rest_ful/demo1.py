from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPagination(CursorPagination):
    # - 根据加密：http: // www.luffycity.com / api / v1 / student /?cursor = erd8
    cursor_query_param = 'cursor'  # 根据什么参数取数据?cursor=1
    ordering = '-created'
    page_size = 2
