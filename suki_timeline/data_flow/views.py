import sqlite3

from django.http import HttpResponse
from django.shortcuts import render
import json
import string

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from data_flow.models import EventModel
from util import tick_to_string, string_to_tick


def render_index(request):
    return render(request, "viewer.html")


def render_editor(request):
    return render(request, "editor.html")


def get_data(request):
    offset = string.atoi(request.GET["offset"])
    page_size = string.atoi(request.GET["n"])
    sql_model = "SELECT id,tick,title,comment FROM data_flow_eventmodel ORDER BY tick LIMIT %d OFFSET %d"
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.execute(sql_model % (page_size, offset))
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return HttpResponse(json.dumps(
        [
            {
                "id": row[0],
                "tick": tick_to_string(row[1]),
                "title": row[2],
                "comment": row[3],
            }
            for row in res
        ]
    ))


@csrf_exempt
def post_data(request):
    try:
        emodel = EventModel.objects.get(id=string.atoi(request.POST["id"]))
        emodel.title = request.POST["title"]
        emodel.comment = request.POST["comment"]
        emodel.tick = string_to_tick(request.POST["tick"])
        emodel.save()
        return HttpResponse(json.dumps(
            {"status": "success"}
        ))
    except:
        return HttpResponse(json.dumps(
            {"status": "fail"}
        ))
