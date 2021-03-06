from django.conf.urls import url

from ComicDatabase.api.v1_0 import api

urlpatterns = [
    url(r'^characters/', api.get_characters),
    url(r'^chapters/', api.get_chapters),
    url(r'^lines/(?P<chapter_number>[0-9.]*)/(?P<page_number>[0-9]+)/new/(?P<character_id>[0-9]+?)/(?P<line_text>.*)/', api.add_line),
    url(r'^lines/(?P<chapter_number>[0-9.]*)/(?P<page_number>[0-9]+)/', api.get_lines),
    url(r'^lines/delete/(?P<id>[0-9]*)/', api.delete_line),
    url(r'^lines/order/(?P<id>[0-9]*)/(?P<difference>[0-9-]*)/', api.change_line_order),
]