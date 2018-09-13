# coding=utf-8

"""
Http 响应常用类
"""

import json
import os
import sys
import time
import traceback
from django.http import HttpResponse


def get_request_with_default(request, key, default_value):
    """
    Try to get value by specific key in request object, if can't find key in keySet, return default value.
    :param request: request object created by django
    :param key: key
    :param default_value: default value
    :return:
    """
    try:
        return request.GET[key]
    except:
        return default_value


def get_request_get(request, key):
    """
    Try to get value by specific key in request object, if can't find key in keySet, return None.
    :param request: request object created by django
    :param key: key
    :return:
    """
    return get_request_with_default(request, key, None)


def get_json_response(obj):
    """
    Create a http response
    :param obj: object which json serializable
    :return:
    """
    response = HttpResponse(json.dumps(obj), content_type="application/json")
    return response


def get_host(request):
    """
    Get host info from request META
    :param request:
    :return:
    """
    return request.META["HTTP_HOST"].split(":")[0]


def response_json_error_info(func):
    """
    Trying to run function, if exception caught, return error details with json format
    :param func:
    :return:
    """

    def wrapper(request):
        try:
            return func(request)
        except Exception as ex:
            print("Error:" + str(ex), file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            return get_json_response({
                "status": "error",
                "error_info": str(ex),
                "trace_back": traceback.format_exc()
            })

    return wrapper


def response_json(func):
    """
    Trying to run function, if exception caught, return error details with json format, else return json formatted object
    :param func:
    :return:
    """

    def wrapper(request):
        try:
            return get_json_response(func(request))
        except Exception as ex:
            print("Error:" + str(ex), file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            return get_json_response({
                "status": "error",
                "error_info": str(ex),
                "trace_back": traceback.format_exc()
            })

    return wrapper


def response_figure_image(func):
    """
    尝试将返回的Figure做成PNG格式的图片
    :param func:
    :return:
    """

    def wrapper(request):
        try:
            fn = "%d.png" % int(time.time() * 1000 * 1000)
            fig = func(request)
            fig.savefig(fn)
            with open(fn, "rb") as fp:
                image_data = fp.read()
            os.remove(fn)
            return HttpResponse(image_data, content_type="image/png")
        except Exception as ex:
            print("Error:" + str(ex), file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            return get_json_response({
                "status": "error",
                "error_info": str(ex),
                "trace_back": traceback.format_exc()
            })

    return wrapper
