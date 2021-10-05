"""
第9章/HomeSharing/app/db/table_auth_membership.py
"""

from pydal import Field


def define_table(db):
    db.define_table(
        "auth_membership",
        Field('group_id', "reference user_group"),
        Field('user_id', "reference user")
    )
