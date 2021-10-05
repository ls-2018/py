from app.db.action_with_db import ActionWithDb
from cms4py.http import Request, Response


class index(ActionWithDb):
    async def execute(self, req: Request, res: Response):
        await res.redirect("/house/all")
