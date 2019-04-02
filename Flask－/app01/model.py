# from flask import request
#
#
# try:
#     from greenlet import getcurrent as get_ident
# except ImportError:
#     try:
#         from thread import get_ident
#     except ImportError:
#         from _thread import get_ident
# print(get_ident())# 140418806785856