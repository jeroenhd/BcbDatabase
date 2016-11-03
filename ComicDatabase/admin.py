# Register your models here.
from django.contrib import admin

from ComicDatabase.models import *

admin.site.register(Chapter)
admin.site.register(Line)
admin.site.register(Character)
admin.site.register(Species)
