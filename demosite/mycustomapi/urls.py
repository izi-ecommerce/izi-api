from django.conf.urls import url
from django.contrib import admin

from izi.app import application as izi

from .app import application as api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', api.urls),
    url(r'', izi.urls),
]
