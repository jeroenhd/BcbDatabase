from django.conf.urls import url

from ComicDatabase import views

app_name = "ComicDatabase"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^c(?P<chapternr>[0-9\.]+)/p(?P<page>[0-9\.]+)/(?P<terms>.*)?$', views.page, name='page'),
    url(r'search/(?P<terms>.*)?/?$', views.search, name='search')
]
