import sqlite3
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import json
import string

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from data_flow.models import EventModel
from util import tick_to_string, string_to_tick


@login_required
def render_index(request):
    return render(request, "viewer.html")


@login_required
def render_editor(request):
    return render(request, "editor.html")


def get_data(request):
    offset = int(request.GET["offset"])
    page_size = int(request.GET["n"])
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


@login_required
@csrf_exempt
def modify_info(request):
    try:
        emodel = EventModel.objects.get(id=int(request.POST["id"]))
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
