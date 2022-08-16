"""
第8章/cms4py_first_generation/app/controllers/lang.py
"""


async def hello(req, res):
    words = res.translate("Hello")
    await res.end(words.encode("utf-8"))
