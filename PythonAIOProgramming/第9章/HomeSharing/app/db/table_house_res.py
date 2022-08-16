"""
第9章/HomeSharing/app/db/table_house_res.py
"""

from pydal import Field


def define_table(db):
    db.define_table(
        "house_res",
        Field('res_title'),
        Field('res_content'),
        Field('pub_time', type='datetime'),
        Field('owner_id', type="reference auth_user")
    )
