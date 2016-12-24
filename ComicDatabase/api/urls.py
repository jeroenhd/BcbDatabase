from django.conf.urls import url, include

from ComicDatabase.api import api

app_name = "Api"

urlpatterns = [
    url(r'^$', api.index, name='index'),
    url(r'^v1.0/', include('ComicDatabase.api.v1_0.urls'))
]