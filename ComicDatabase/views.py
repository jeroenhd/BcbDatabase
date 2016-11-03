from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("dootdoot dootdoot doot doot")


# Create your views here.
def page(request, chapter, page):
    return render(request, 'ComicDatabase/page.html', {'chapter': chapter, 'page': page})
