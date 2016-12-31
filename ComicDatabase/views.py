from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from ComicDatabase.classes import SearchForm
from ComicDatabase.models import Line, Chapter, Character


def nav(request, chapter=None, page_=None, terms=None):
    """Render the navigation view"""
    return render_to_string('ComicDatabase/nav.html',
                            {'chapter': chapter, 'page': page_, 'terms': terms, 'user': request.user})


def index(request):
    return HttpResponse("dootdoot dootdoot doot doot")


# Create your views here.
def page(request, chapternr, page, terms):
    chapter = Chapter.objects.filter(number=chapternr).first()

    lines = Line.objects.filter(chapter__number=chapter.number, page=page).order_by('order')

    navbox = nav(request, chapter, page, terms)

    if float(chapter.number) == int(float(chapter.number)):
        chapter.number = int(float(chapter.number))

    return render(request, 'ComicDatabase/page.html',
                  {'chapter': chapter, 'page': page, 'terms': terms, 'lines': lines, 'nav': navbox})


@login_required
def page_edit(request, chapternr, page, terms):
    chapter = Chapter.objects.filter(number=chapternr).first()

    lines = Line.objects.filter(chapter__number=chapter.number, page=page).order_by('order')

    navbox = nav(request, chapter, page, terms)

    if float(chapter.number) == int(float(chapter.number)):
        chapter.number = int(float(chapter.number))

    characters = Character.objects.all()

    return render(request, 'ComicDatabase/page_admin.html',
                  {'chapter': chapter, 'page': page, 'terms': terms, 'lines': lines, 'nav': navbox, 'characters': characters})


def search(request, terms=None):
    """List search results"""

    if request.method == 'POST':
        return HttpResponseRedirect(reverse('ComicDatabase:search', args=(request.POST.get('terms'),)))
    else:
        form = SearchForm()

    results = Line.objects.filter(text__search=terms)
    navblock = nav(request)
    return render(request, 'ComicDatabase/search.html',
                  {'results': results, 'terms': terms, 'nav': navblock, 'form': form})
