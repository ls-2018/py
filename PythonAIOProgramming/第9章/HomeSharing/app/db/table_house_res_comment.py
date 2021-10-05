"""
第9章/HomeSharing/app/db/table_house_res_comment.py
"""

from pydal import Field


def define_table(db):
    db.define_table(
        "house_res_comment",
        Field('user_id', type="reference auth_user"),
        Field('house_res_id', type="reference house_res"),
        Field('comment_content'),
        Field('comment_time', type='datetime')
    )
