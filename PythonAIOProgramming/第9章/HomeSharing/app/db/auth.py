"""
第9章/HomeSharing/app/db/auth.py
"""

from cms4py.http import Request


async def has_membership(db, request, response, role, user_id=None):
    """
    根据用户id或者当前登录的用户判断是否属于指定的组
    :param db: PyDALCursor 对象
    :param request:
    :param response:
    :param role:
    :param user_id:
    :return:
    """
    if not user_id:
        current_user = await request.get_session("current_user")
        user_id = current_user['id'] \
            if (current_user and 'id' in current_user) \
            else None
    if not user_id:
        return False
    return not (await db(
        (db.auth_group.role == role) &
        (db.auth_membership.user_id == user_id) &
        (db.auth_group.id == db.auth_membership.group_id)
    ).isempty())


def require_login():
    """
    目标 Action 的访问要求用户登录
    :return:
    """

    def outer(func):
        async def wrapper(*args):
            argc = len(args)
            if argc == 3:
                req: Request = args[1]
                res = args[2]
            elif argc == 2:
                req: Request = args[0]
                res = args[1]
            else:
                raise TypeError()
            # 如果已登录，则执行目标函数
            if await req.get_session('current_user'):
                return await func(*args)
            # 如果未登录，则跳转到登录页面
            else:
                await res.redirect("/user/login")

        return wrapper

    return outer


def require_membership(*roles):
    """
    目标 Action 要求用户在指定的组里，目标 Action 必须
    是 ActionWithDb 类型
    :param roles:
    :return:
    """

    def outer(func):
        async def inner(action_with_db, request: Request, response):
            if await request.get_session("current_user"):
                for r in roles:
                    if await has_membership(
                            action_with_db.db, request, response, r
                    ):
                        await func(action_with_db, request, response)
                        return
                await response.end(b"Access Denied")
            else:
                await response.redirect("/user/login")

        return inner

    return outer


async def add_membership(db, request, response, user_id, role):
    """
    添加用户关系
    :param db:
    :param request:
    :param response:
    :param user_id: 指定的用户id
    :param role: 指定的权限组名
    :return:
    """
    group = (await db(db.auth_group.role == role).select()).first()
    if group:
        await db.auth_membership.insert(user_id=user_id, group_id=group.id)


async def remove_membership(db, request, response, user_id, role):
    """
    移除用户关系
    :param db:
    :param request:
    :param response:
    :param user_id: 用户id
    :param role: 权限组名
    :return:
    """
    group = (await db(db.auth_group.role == role).select()).first()
    if group:
        await db(
            (db.auth_membership.user_id == user_id) &
            (db.auth_membership.group_id == group.id)
        ).delete()
