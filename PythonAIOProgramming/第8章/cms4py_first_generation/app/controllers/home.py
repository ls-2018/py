"""
第8章/cms4py_first_generation/app/controllers/home.py
"""


async def index(req, res):
    await res.render("home/index.html")
