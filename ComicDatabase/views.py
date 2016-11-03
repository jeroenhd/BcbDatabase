from django.http import HttpResponse
from django.shortcuts import render

from ComicDatabase.models import Line


def index(request):
    return HttpResponse("dootdoot dootdoot doot doot")


# Create your views here.
def page(request, chapter, page):
    lines = Line.objects.filter(chapter__number=chapter, page=page).order_by('order')
    return render(request, 'ComicDatabase/page.html', {'chapter': chapter, 'page': page, 'lines': lines})
