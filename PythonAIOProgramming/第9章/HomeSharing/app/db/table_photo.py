"""
第9章/HomeSharing/app/db/table_photo.py
"""

from pydal import Field


def define_table(db):
    db.define_table(
        "photo",
        Field('photo_name'),
        Field('photo_uri'),
        Field('photo_path'),
        Field('creator', type="reference auth_user"),
        Field('creation_time', type="datetime"),
    )
