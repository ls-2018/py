"""
第9章/HomeSharing/app/db/data_grid.py
"""

from typing import Awaitable
from cms4py.http import Request, Response
import config
from urllib.parse import unquote
import math
import inspect
from app.utils import url


def default_row_render(db, request, response, row, fields):
    html_str = "<tr>"
    for f in fields:
        html_str += f"<td>{row[f]}</td>"
    html_str += "</tr>"
    return html_str


def default_header_render(db, request, response, fields):
    html_str = "<tr>"
    for f in fields:
        html_str += f"<th>{response.translate(f)}</th>"
    html_str += "</tr>"
    return html_str


def default_foot_render(
        db,
        request: Request,
        response,
        current_page_index,
        paginate, all_count
):
    """
    默认的底部选择器链接渲染器，算法为根据当前页码向左最多呈现5个页码
    链接，向右最多呈现5个页码链接
    :param db:
    :param request:
    :param response:
    :param current_page_index:
    :param paginate:
    :param all_count:
    :return:
    """
    vars = {}
    for k in request.query_vars:
        vars[k.decode(config.GLOBAL_CHARSET)] = unquote(
            request.get_query_var(k).decode(config.GLOBAL_CHARSET)
        )

    def create_link(page_index, label=None, active=False):
        vars['page_index'] = page_index
        return f"<li class=\"page-item {'active' if active else ''}\">" \
               f"  <a " \
               f"    class=\"btn-page-number page-link\" " \
               f"    href='{request.path}?{url.dict_to_url_params(vars)}'>" \
               f"      {(page_index + 1) if not label else label}" \
               f"  </a>" \
               f"</li>"

    last_page_index = math.ceil(all_count / paginate) - 1
    html_str = ""
    if last_page_index > 0:
        page_number_btns = [create_link(current_page_index, active=True)]
        i = 0
        for i in range(current_page_index - 1, current_page_index - 5, -1):
            if i < 0:
                break
            page_number_btns.insert(0, create_link(i))
        if i > 0:
            page_number_btns.insert(0, create_link(0, "<<"))
        for i in range(current_page_index + 1, current_page_index + 5):
            if i > last_page_index:
                break
            page_number_btns.append(create_link(i))
        if i < last_page_index:
            page_number_btns.append(create_link(last_page_index, ">>"))
        # dump html content
        html_str += " ".join(page_number_btns)
    return html_str


async def grid(
        db,
        request: Request,
        response: Response,
        query,
        fields=None,
        order_by=None,
        paginate=20,
        row_render=default_row_render,
        header_render=default_header_render,
        foot_render=default_foot_render
):
    """
    生成分页的表格，原理是获取页面中的页码参数，以查询数据库，
    并根据页码生成对应底部选择器
    :param db:
    :param request:
    :param response:
    :param query: 该表格对应的查询语句
    :param fields: 要呈现的字段，默认为全部字段
    :param order_by: 排序方式
    :param paginate: 每页数据条数
    :param row_render: 行渲染器，用于自定义行内容
    :param header_render: 表头渲染器，用于自定义表头
    :param foot_render: 底部选择器渲染器，用于自定义选择器
    :return:
    """
    page_index = int(request.get_query_var(b"page_index", b"0"))

    # 获取符合条件的所有数据的条数，用于计算分页
    all_count = await db(query).count()

    # 如果外部指定了字段，则呈现指定的字段数据
    if fields:
        db_rows = await db(query).select(
            *fields,
            limitby=(paginate * page_index, (page_index + 1) * paginate),
            orderby=order_by
        )
    # 如果外部没有指定字段，则呈现所有字段数据
    else:
        db_rows = await db(query).select(
            limitby=(paginate * page_index, (page_index + 1) * paginate),
            orderby=order_by
        )

    table_body_rows_html_content = ""
    # 渲染表中的行
    for r in db_rows:
        row_render_result = row_render(
            db, request, response, r, db_rows.field_names
        )
        if isinstance(row_render_result, Awaitable):
            row_render_result = await row_render_result

        if isinstance(row_render_result, str):
            row_content = row_render_result
        elif isinstance(row_render_result, bytes):
            row_content = row_render_result.decode("utf-8")
        else:
            row_content = ''
        table_body_rows_html_content += row_content

    rendered_header_content = ''
    rendered_header_result = header_render(
        db, request, response, db_rows.field_names
    )
    if inspect.isawaitable(rendered_header_result):
        rendered_header_content = await rendered_header_result
    else:
        rendered_header_content = rendered_header_result
    if isinstance(rendered_header_content, str):
        table_header_html_content = rendered_header_content
    elif isinstance(rendered_header_content, bytes):
        table_header_html_content = rendered_header_content.decode("utf-8")
    else:
        table_header_html_content = ""

    table_html_content = \
        f"<div>" \
        f"  <div>" \
        f"    <table class='data-grid table'>" \
        f"      <thead>{table_header_html_content}</thead>" \
        f"      <tbody>{table_body_rows_html_content}</tbody>" \
        f"    </table>" \
        f"  </div>" \
        f"  <div class='page-numbers-container'>" \
        f"    <nav>" \
        f"      <ul class='pagination'>" \
        f"        {foot_render(db, request, response, page_index, paginate, all_count)}" \
        f"      </ul>" \
        f"    </nav>" \
        f"  </div>" \
        f"</div>"

    return table_html_content
