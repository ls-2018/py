"""
第9章/HomeSharing/app/db/table_auth_user.py
"""

from pydal import Field
from pydal.validators import CRYPT


def define_table(db):
    db.define_table(
        "auth_user",
        Field("user_name"),
        Field("user_password", requires=CRYPT()),
        Field("user_email"),
        Field("user_phone"),
        Field("reg_time", type="datetime"),
    )
    pass
