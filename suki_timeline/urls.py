# -*- coding: utf-8 -*-
"""suki_timeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import data_flow.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^$', data_flow.views.render_index),
    url(r'^editor/', data_flow.views.render_editor),
    url(r'^images/get/info', data_flow.views.get_image_info),
    url(r'^images/get/thumbnail', data_flow.views.get_image_resize),
    url(r'^images/get/raw', data_flow.views.get_image),

    url(r'^images/query', data_flow.views.query_images),
    url(r'^image/modify', data_flow.views.modify_image),
    url(r'^image/rotate', data_flow.views.rotate),
    url(r'^image/delete', data_flow.views.remove_image),
    url(r'^image/upload', data_flow.views.upload_file),
]
