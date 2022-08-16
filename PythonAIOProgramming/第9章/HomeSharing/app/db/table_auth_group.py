"""
第9章/HomeSharing/app/db/table_auth_group.py
"""

from pydal import Field


def define_table(db):
    db.define_table(
        "auth_group",
        Field('role'),
        Field('description'),
    )
    pass
