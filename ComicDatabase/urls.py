from django.conf.urls import url, include

from ComicDatabase import auth_views
from ComicDatabase import views

app_name = "ComicDatabase"
urlpatterns = [
    url(r'^api/', include('ComicDatabase.api.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^c(?P<chapternr>[0-9\.]+)/p(?P<page>[0-9\.]+)/(?P<terms>.*)?$', views.page, name='page'),
    url(r'^a/c(?P<chapternr>[0-9\.]+)/p(?P<page>[0-9\.]+)/(?P<terms>.*)?$', views.page_edit, name='page_edit'),
    url(r'^search/(?P<terms>.*)?/?$', views.search, name='search'),
    url(r'^accounts/login/.*', auth_views.login_page, name='login'),
    url(r'^accounts/logout/.*', auth_views.logout_page, name='logout')
]
