from django.conf.urls import url

from ComicDatabase import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^c(?P<chapter>[0-9\.]+)/p(?P<page>[0-9\.]+)/$', views.page, name='page'),
]
