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
from django.conf.urls import url
from django.contrib import admin
import data_flow.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', data_flow.views.render_index),

    url(r'^get/data/timeline', data_flow.views.get_data),

    # 生产环境需要注释掉这两行
    url(r'^editor/', data_flow.views.render_editor),
    url(r'^post/data/timeline', data_flow.views.post_data),
]
