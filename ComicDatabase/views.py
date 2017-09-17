from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from ComicDatabase.classes import SearchForm
from ComicDatabase.models import Line, Chapter, Character


def nav(request, chapter_=None, page_=None, terms=None, editing=False):
    """Render the navigation view"""

    all_chapters = Chapter.objects.all()

    return render_to_string('ComicDatabase/nav.html',
                            {'chapter': chapter_, 'page': page_, 'terms': terms, 'user': request.user, 'editing': editing, 'all_chapters': all_chapters}, request)


def index(request):
    return render(request, 'ComicDatabase/index_list.html', {
        'nav': nav(request), 'chapters': Chapter.objects.all()
    })


# Create your views here.
def page(request, chapternr, page, terms):
    current_chapter = Chapter.objects.filter(number=chapternr).first()  # type: Chapter

    lines = Line.objects.filter(chapter__number=current_chapter.number, page=page).order_by('order')

    nav_box = nav(request, current_chapter, page, terms)

    if float(current_chapter.number) == int(float(current_chapter.number)):
        current_chapter.number = int(float(current_chapter.number))

    page = int(page)

    new_chapter = None

    if page < 1:
        new_chapter = Chapter.objects.filter(number__lt=chapternr).first()
        if new_chapter is None:
            new_chapter = current_chapter
        page = new_chapter.pageCount
    if page > current_chapter.pageCount:
        new_chapter = Chapter.objects.filter(number__gt=chapternr).order_by('number').first()
        if new_chapter is None:
            new_chapter = current_chapter
        page = 1

    if new_chapter is not None:
        current_chapter = new_chapter

    return render(request, 'ComicDatabase/page.html',
                  {'chapter': current_chapter, 'page': page, 'terms': terms, 'lines': lines, 'nav': nav_box})


@login_required
def page_edit(request, chapternr, page, terms):
    chapter = Chapter.objects.filter(number=chapternr).first()

    lines = Line.objects.filter(chapter__number=chapter.number, page=page).order_by('order')

    nav_box = nav(request, chapter, page, terms, True)

    if float(chapter.number) == int(float(chapter.number)):
        chapter.number = int(float(chapter.number))

    characters = Character.objects.all()
    chars = []
    for i in range(0, len(characters)):
        characters[i].line_count = Line.objects.filter(character=characters[i]).count()

        chars.append(characters[i])

    chars.sort(key=lambda x: -x.line_set.count())

    return render(request, 'ComicDatabase/page_admin.html',
                  {'chapter': chapter, 'page': page, 'terms': terms, 'lines': lines, 'nav': nav_box,
                   'characters': chars})


def search(request, terms=None):
    """List search results"""

    if request.method == 'POST':
        return HttpResponseRedirect(reverse('ComicDatabase:search', args=(request.POST.get('terms'),)))
    else:
        form = SearchForm()

    results = Line.objects.filter(text__search=terms)
    nav_box = nav(request, None, None, terms)
    return render(request, 'ComicDatabase/search.html',
                  {'results': results, 'terms': terms, 'nav': nav_box, 'form': form})


def chapter(request, chapter_number):
    """
    Show information about a chapter
    :param request: The Django request passed to the call
    :param chapter_number: The chapter number to show info about
    :return:
    """
    c = Chapter.objects.filter(number=chapter_number).first()  # type: Chapter
    if c is None:
        raise Http404('No chapter found for chapter number ' + chapter_number)

    pages = []
    for p in range(1, c.pageCount + 1):
        lines = Line.objects.filter(chapter__number=c.number, page=p)
        line_count = lines.count()

        characters = Character.objects.filter(
            line__chapter__number=chapter_number,
            line__page=p
        ).annotate(line_count=Count('line')).order_by('-line_count','name').all()

        pages.append({'number': p, 'line_count': line_count, 'characters': characters})

    return render(request, 'ComicDatabase/index_chapter.html', {
        'nav': nav(request, c), 'pages': pages, 'chapter': c
    })
