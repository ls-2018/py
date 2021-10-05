"""
第8章/cms4py_first_generation/app/db/__init__.py
"""

from app.db.async_pydal.dal import AsyncDAL
from . import table_auth_group
from . import table_auth_membership
from . import table_auth_user
from . import table_photo
from . import table_house_res
from . import table_house_res_comment


class Db:
    __instance = None

    @staticmethod
    async def get_instance() -> "Db":
        if not Db.__instance:
            Db.__instance = Db()
            await Db.__instance._async_init()
        return Db.__instance

    async def _async_init(self):
        self._async_pydal = await AsyncDAL.create(
            "db", "root", "rootpw", "home_sharing"
        )

        table_auth_user.define_table(self._async_pydal)
        table_auth_group.define_table(self._async_pydal)
        table_auth_membership.define_table(self._async_pydal)
        table_photo.define_table(self._async_pydal)
        table_house_res.define_table(self._async_pydal)
        table_house_res_comment.define_table(self._async_pydal)
        pass

    @property
    def async_pydal(self):
        return self._async_pydal

    pass
