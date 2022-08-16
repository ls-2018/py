"""
第9章/HomeSharing/app/controllers/house.py
"""
from app.db import data_grid
from app.db.action_with_db import ActionWithDb
from cms4py.http import Request
import datetime


class by_id(ActionWithDb):
    async def execute(self, req: Request, res):
        house_id = req.arg(0)
        house = await self.db.house_res.by_id(house_id)
        owner = None
        comments_grid = ""

        async def row_render(db, req, res, row, fields):
            return await res.render_string(
                "house/comment_row.html",
                row=row
            )

        if house:
            owner = await self.db.auth_user.by_id(house['owner_id'])

            if req.method == 'POST':
                # 如果是POST请求，则尝试读取评论数据
                comment = req.get_var_as_str(b"comment")
                if comment:
                    await self.db.house_res_comment.insert(
                        user_id=owner['id'],
                        house_res_id=house['id'],
                        comment_content=comment,
                        comment_time=datetime.datetime.now()
                    )
            db = self.db
            comments_grid = await data_grid.grid(
                db, req, res,
                (db.house_res_comment.house_res_id == house['id']) &
                (db.house_res_comment.user_id == db.auth_user.id),
                fields=[
                    # 只显示指定的字段
                    db.house_res_comment.id,
                    db.house_res_comment.comment_content,
                    db.house_res_comment.comment_time,
                    db.auth_user.user_name
                ],
                order_by=~db.house_res_comment.id,
                row_render=row_render,
                header_render=lambda *args: ""
            )
        await res.render(
            "house/by_id.html",
            title=house['res_title'] if house else '找不到房源',
            house=house,
            owner=owner,
            comments_grid=comments_grid
        )


class all(ActionWithDb):

    async def execute(self, req, res):
        async def row_render(db, req, res, row, fields):
            return await res.render_string(
                "house/all_row.html",
                row=row
            )

        db = self.db
        grid = await data_grid.grid(
            db, req, res,
            # 多表查询
            (db.house_res.id > 0) &
            (db.house_res.owner_id == db.auth_user.id),
            fields=[
                # 只显示指定的字段
                db.house_res.id,
                db.house_res.res_title,
                db.house_res.pub_time,
                db.auth_user.user_name,
                db.auth_user.user_phone,
            ],
            order_by=~db.house_res.id,
            row_render=row_render,
            header_render=lambda *args: ""
        )
        await res.render(
            "house/all.html",
            title="房源", grid=grid
        )
        pass


class search(ActionWithDb):
    async def execute(self, req: Request, res):
        keyword = req.get_var_as_str(b"k")

        async def row_render(db, req, res, row, fields):
            return await res.render_string(
                "house/all_row.html",
                row=row
            )

        db = self.db
        grid = await data_grid.grid(
            db, req, res,
            # 根据指定的关键字查询数据库
            (
                    (db.house_res.res_title.like(f"%{keyword}%")) |
                    (db.house_res.res_content.like(f"%{keyword}%"))
            ) &
            (db.house_res.owner_id == db.auth_user.id),
            fields=[
                # 只显示指定的字段
                db.house_res.id,
                db.house_res.res_title,
                db.house_res.pub_time,
                db.auth_user.user_name,
                db.auth_user.user_phone,
            ],
            order_by=~db.house_res.id,
            row_render=row_render,
            header_render=lambda *args: ""
        )
        await res.render(
            "house/all.html",
            title=f"搜索结果 - {keyword}", grid=grid
        )
        pass
