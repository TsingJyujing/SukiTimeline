import os
import shutil
import sqlite3
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from util.http_response import response_json
from data_flow.models import EventModel
from util import tick_to_string, string_to_tick
from util.request_util import get_default


@login_required
def render_index(request):
    return render(request, "viewer.html")


@login_required
def render_editor(request):
    current_page = int(get_default(request.GET, "n", "0"))
    keywords = get_default(request.GET, "q", "")
    return render(request, "editor.html", {
        "current_page": current_page,
        "keywords": keywords
    })


@response_json
def query_images(request):
    """
    获取图片元数据的接口
    :param request:
    :return:
    """

    def generate_where(keywords: list) -> str:
        if len(keywords) == 0:
            return ""
        else:
            return " WHERE " + " AND ".join([
                "(title like '%{}%' OR comment like '%{}%' )".format(k, k) for k in keywords
            ])

    try:
        keyword_raw = request.GET["keywords"]
        if keyword_raw == "":
            keyword_list = []
        else:
            keyword_list = keyword_raw.split(" ")
    except:
        keyword_list = []
    offset = int(request.GET["offset"])
    page_size = int(request.GET["n"])
    sql_model = "SELECT id,tick,title,comment FROM data_flow_eventmodel %s ORDER BY tick LIMIT %d OFFSET %d"
    sql_exe = sql_model % (generate_where(keyword_list), page_size, offset)
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.execute(sql_exe)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": row[0],
            "tick": tick_to_string(row[1]),
            "title": row[2],
            "comment": row[3],
        }
        for row in res
    ]


@login_required
@response_json
def modify_image(request):
    event_model = EventModel.objects.get(id=int(request.POST["id"]))
    event_model.title = request.POST["title"]
    event_model.comment = request.POST["comment"]
    event_model.tick = string_to_tick(request.POST["tick"])
    event_model.save()
    return {
        "status": "success"
    }


@login_required
@response_json
def remove_image(request):
    image_id = int(request.POST["id"])
    event_model = EventModel.objects.get(id=image_id)
    # 转储源文件，删除缩略图
    shutil.move("static/image/%d.jpg" % image_id, "trash/%d.jpg" % image_id)
    os.remove("static/image/%d_thumbnail.jpg" % image_id)
    # 删除数据库记录
    event_model.delete()
    return {"status": "success"}
