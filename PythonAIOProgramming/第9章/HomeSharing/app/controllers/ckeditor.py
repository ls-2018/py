"""
第9章/HomeSharing/app/controllers/ckeditor.py
"""
import json

from app.db.action_with_db import ActionWithDb
from cms4py.utils import aiofile
from app.db import auth
import os, config, datetime


class file_upload_url(ActionWithDb):

    async def execute(self, req, res):
        user = await req.get_session("current_user")
        if not user:
            # 如果用户没有登录，则提示错误
            await res.end(
                json.dumps(
                    dict(
                        error="User not logged",
                        uploaded=False
                    )
                ).encode("utf-8")
            )
            return

        f = req.get_body_var(b"upload")
        current_datetime = datetime.datetime.now()
        # file_path 是文件路径，用于作为文件存储在服务器的相对路径
        file_path = "u{}d{}{}".format(
            user["id"],
            current_datetime.strftime("%Y%m%d%H%M%S"),
            current_datetime.microsecond
        )
        file_uri = "{}/{}".format(
            config.UPLOAD_FILE_BASE_URI,
            file_path
        )
        fw = await aiofile.open_async(
            os.path.join(
                config.UPLOADS_ROOT,
                file_path
            ),
            "wb"
        )
        await fw.write(f['content'])
        await fw.close()
        await self.db.photo.insert(
            photo_name=f['filename'],
            photo_path=file_path,
            photo_uri=file_uri,
            creator=user['id'],
            creation_time=current_datetime
        )
        await res.end(
            json.dumps(
                dict(
                    error=None,
                    uploaded=True,
                    url=file_uri
                )
            ).encode("utf-8")
        )
