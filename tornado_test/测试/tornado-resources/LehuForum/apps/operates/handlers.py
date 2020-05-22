import json

from LehuForum.handlers import RedisHandler
from apps.operates.models import Message, MESSAGE_TYPE
from apps.users.models import User
from apps.utils.async_decorators import authenticated_async


class MessageHandler(RedisHandler):
    @authenticated_async
    async def get(self, *args, **kwargs):
        """获取当前登录用户的消息"""
        ret_data = []
        type_list = self.get_query_arguments("msg_type", [])
        if type_list:
            message_query = Message.filter(Message.reciever_id == self.current_user.id,
                                           Message.msg_type.in_(type_list))
        else:
            message_query = Message.filter(Message.reciever_id == self.current_user.id)

        messages = await self.application.objects.execute(message_query)
        for msg in messages:
            sender = await self.application.objects.get(User, id=msg.sender_id)
            item_dict = dict()
            item_dict['sender'] = {
                "id": sender.id,
                "nick_name": sender.nick_name,
                "head_url": "{}/media/{}".format(self.settings["SITE_URL"], sender.head_url)
            }
            item_dict['reciever'] = {
                "id": self.current_user.id,
                "nick_name": self.current_user.nick_name,
                "head_url": "{}/media/{}".format(self.settings["SITE_URL"], self.current_user.head_url)
            }
            item_dict['msg_type'] = MESSAGE_TYPE[msg.msg_type-1][1]
            item_dict['message'] = msg.message
            item_dict['parent'] = msg.parent
            item_dict['add_time'] = msg.add_time.strftime("%Y-%m-%d %H:%M")

            ret_data.append(item_dict)

        self.finish(json.dumps(ret_data))