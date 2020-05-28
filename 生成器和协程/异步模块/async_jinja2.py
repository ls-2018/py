#!/usr/bin/env python
import sys
from jinja2 import Environment, PackageLoader, select_autoescape
from sanic import Blueprint
from sanic.response import html

# https://github.com/channelcat/sanic/blob/5bb640ca1706a42a012109dc3d811925d7453217/examples/jinja_example/jinja_example.py
# 开启异步特性  要求3.6+
enable_async = sys.version_info >= (3, 6)
html_bp = Blueprint("async_html")
html_bp.static('/statics/rss_html', '/root/statics/rss_html')

# jinjia2 config
env = Environment(
    loader=PackageLoader('src.views.rss_html', '../templates/rss_html'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']),
    enable_async=enable_async)


async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    rendered_template = await template.render_async(**kwargs)
    return html(rendered_template)


@html_bp.route("/")
async def index(request):
    return await template('index.html')
