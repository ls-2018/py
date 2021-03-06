# _*_coding:utf-8_*_

import time
import hashlib
import json
from assets import models
from django.shortcuts import HttpResponse
from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist


def json_date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d")


def json_datetime_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d %H:%M:%S")


def gen_token(username, timestamp, token):
    token_format = "%s\n%s\n%s" % (username, timestamp, token)
    obj = hashlib.md5()
    obj.update(bytes(token_format, encoding='utf8'))
    # print("token format:[%s]" % token_format)
    # print("token :[%s]" % obj.hexdigest())
    return obj.hexdigest()[10:17]


def token_required(func):
    def wrapper(*args, **kwargs):
        response = {"errors": []}
        # args[0] = request
        get_args = args[0].GET
        username = get_args.get("user")
        token_md5_from_client = get_args.get("md5_token")
        timestamp = get_args.get("timestamp")
        if not username or not timestamp or not token_md5_from_client:
            response['errors'].append({"auth_failed": "This api requires token authentication!"})
            return HttpResponse(json.dumps(response))
        try:
            user_obj = models.UserProfile.objects.get(name=username)
            token_md5_from_server = gen_token(username, timestamp, user_obj.token)
            if token_md5_from_client != token_md5_from_server:
                response['errors'].append({"auth_failed": "Invalid username or token_id"})
            else:
                if abs(time.time() - int(timestamp)) > settings.TOKEN_TIMEOUT:  # default timeout 120
                    response['errors'].append({"auth_failed": "The token is expired!"})
                else:

                    print("\033[31;1mPass authentication\033[0m")
        except ObjectDoesNotExist:
            response['errors'].append({"auth_failed": "Invalid username or token_id"})
        if response['errors']:
            return HttpResponse(json.dumps(response))
        else:
            return func(*args, **kwargs)

    return wrapper
