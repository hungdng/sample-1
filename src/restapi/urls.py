"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from updates.views import update_model_detail_view, JsonCBV, JsonCBV2, SerializedListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', update_model_detail_view),
    url(r'^json/cbv/$', JsonCBV.as_view()),
    url(r'^json/cbv2/$', JsonCBV2.as_view()),
    url(r'^json/serialized/list/$', SerializedListView.as_view()),
]
