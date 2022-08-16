"""
第9章/HomeSharing/app/controllers/admin.py
"""
from cms4py.http import Request
from ..db import auth
from ..db import data_grid
from ..db.action_with_db import ActionWithDb


class index(ActionWithDb):

    @auth.require_membership("admin")
    async def execute(self, req, res):
        await res.render("admin/index.html", title="cms4py管理面板")


class memberships(ActionWithDb):

    @auth.require_membership("admin")
    async def execute(self, req, res):
        db = self.db
        grid = await data_grid.grid(
            db, req, res,
            db.auth_membership.id > 0,
            order_by=~db.auth_membership.id
        )
        await res.render(
            "admin/memberships.html", title="关系表",
            grid=grid
        )


class groups(ActionWithDb):

    @auth.require_membership("admin")
    async def execute(self, req, res):
        async def header_render(db, req, res, fields):
            return await res.render_string(
                "admin/groups_header.html"
            )

        async def row_render(db, req, res, row, fields):
            return await res.render_string(
                "admin/groups_row.html",
                row=row
            )

        db = self.db
        grid = await data_grid.grid(
            db, req, res,
            db.auth_group.id > 0,
            order_by=~db.auth_group.id,
            row_render=row_render,
            header_render=header_render
        )
        await res.render(
            "admin/groups.html",
            title="用户组管理", grid=grid
        )


class edit_group(ActionWithDb):

    async def execute(self, req: Request, res):
        db = self.db
        group_id = req.get_var_as_str(b"group_id")
        group_role = req.get_var_as_str(b"role")
        group_description = req.get_var_as_str(b"description")

        if not await auth.has_membership(db, req, res, 'admin'):
            await res.end(b"AccessDenied")
            return

        if not group_id:
            # 如果没有指定 id，则创建新组
            await db.auth_group.insert(
                role=group_role,
                description=group_description
            )
        else:
            # 如果已指定 id，则更新指定的组
            await db(db.auth_group.id == group_id).update(
                description=group_description
            )
        await res.end(b"ok")


class users(ActionWithDb):

    @auth.require_membership("admin")
    async def execute(self, req, res):
        async def header_render(db, req, res, fields):
            return await res.render_string(
                "admin/users_header.html"
            )

        async def row_render(db, req, res, row, fields):
            return await res.render_string(
                "admin/users_row.html",
                row=row
            )

        db = self.db
        grid = await data_grid.grid(
            db, req, res,
            db.auth_user.id > 0,
            order_by=~db.auth_user.id,
            row_render=row_render,
            header_render=header_render
        )
        await res.render(
            "admin/users.html",
            title="所有用户", grid=grid
        )


class manage_permissions(ActionWithDb):

    @auth.require_membership('admin')
    async def execute(self, request, response):
        user = await self.db.auth_user.by_id(
            request.get_var_as_str(b"userid")
        )
        if user:
            groups = await self.db(self.db.auth_group.id > 0).select()
            for g in groups:
                g.row_data['has_membership'] = await auth.has_membership(
                    self.db, request, response, g.role,
                    user.id
                )
            await response.render(
                "admin/manage_permissions.html",
                the_user=user,
                groups=groups,
                title='权限管理'
            )
        else:
            await response.end(b"User not found.")


class edit_membership(ActionWithDb):

    @auth.require_membership('admin')
    async def execute(self, request, response):
        operation = request.get_var_as_str(b"op")
        role = request.get_var_as_str(b"role")
        userid = request.get_var_as_str(b"userid")
        current_user = await request.get_session("current_user")
        if operation == 'add_membership':
            await auth.add_membership(
                self.db, request, response, userid, role
            )
            await response.redirect(
                f"/admin/manage_permissions?userid={userid}"
            )
        elif operation == "remove_membership":
            if userid != str(current_user['id']) or role != 'admin':
                await auth.remove_membership(
                    self.db, request, response, userid, role
                )
                await response.redirect(
                    f"/admin/manage_permissions?userid={userid}"
                )
            else:
                await response.end(
                    b"You can not remove the admin membership of yourself"
                )
        else:
            await response.end(b"Unsupported action")
