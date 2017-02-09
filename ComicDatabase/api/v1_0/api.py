import sys

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from ComicDatabase.models import Character, Chapter, Line


def get_characters(request):
    characters_raw = Character.objects.all()
    characters = []

    for c in characters_raw:
        characters.append({
            'id': c.id,
            'name': c.name,
            'species': c.species_id,
        })

    result = {'Result': 'OK', 'characters': characters}
    return JsonResponse(result)


def get_chapters(request):
    chapters_raw = Chapter.objects.all()
    chapters = []
    for c in chapters_raw:
        chapters.append({
            'number': c.number,
            'title': c.title,
            'description': c.description
        })

    return JsonResponse({'Result': 'OK', 'chapters': chapters})


def get_lines(request, chapter_number, page_number):
    lines_raw = Line.objects.filter(page=page_number, chapter__number=chapter_number)

    lines = []
    for l in lines_raw:
        lines.append({
            'id': l.id,
            'chapter': l.chapter.number,
            'page': l.page,
            'character': l.character.id,
            'text': l.text,
            'order': l.order
        })

    return JsonResponse({'Result': 'OK', 'lines': lines})


@login_required
def add_line(request, chapter_number, page_number, character_id, line_text):
    if not request.user.is_authenticated():
        return JsonResponse({'Result': 'Fail', 'reason': 'Log in to execute this action'})
    try:
        chapter_number = float(chapter_number)
        page_number = int(page_number)
        character_id = int(character_id)
        latest_line_query = Line.objects.filter(chapter__number=chapter_number, page=page_number)

        try:
            order = latest_line_query.latest('order').order
            order += 1
        except ObjectDoesNotExist:
            order = 0

        newline = Line()

        newline.chapter = Chapter.objects.filter(number=chapter_number).first()

        newline.character = Character.objects.filter(id=character_id).first()
        if newline.chapter is None or newline.character is None:
            raise Exception('Invalid chapter or character')

        newline.page = page_number
        if page_number < 1 or page_number > newline.chapter.pageCount:
            raise Exception('Invalid page number')

        newline.text = line_text
        newline.order = order

        newline.save()

        return JsonResponse({'Result': 'OK', 'character': {'id': newline.character.id, 'name': newline.character.name,
                                                           'species': newline.character.species_id},
                             'line': newline.text, 'order': newline.order, 'id': newline.pk})
    except:
        e = sys.exc_info()[0]
        return JsonResponse({'Result': 'Fail', 'reason': str(e)})


@login_required
def delete_line(request, id):
    if not request.user.is_authenticated():
        return JsonResponse({'Result': 'Fail', 'reason': 'Log in to execute this action'})
    try:
        int_id = int(id)
        line = Line.objects.filter(id=int_id).first()  # type: Line
        line.delete()

        return JsonResponse({'Result': 'OK'})
    except:
        e = sys.exc_info()[0]
        return JsonResponse({'Result': 'Fail', 'reason': str(e)})


@login_required
def change_line_order(request, id, difference):
    id = int(id)
    difference = int(difference)

    line = Line.objects.filter(id=id).first()  # type: Line
    old_order = line.order
    new_order = line.order + difference

    swap_with = Line.objects. \
        filter(page=line.page, chapter__number=line.chapter.number, order=new_order). \
        first()  # type: Line

    # Check if the line we're swapping the selected line with exists
    if swap_with is None:
        # It doesn't, hmm...
        if difference < 0:
            # We're all the way to the top!
            return JsonResponse({'Result': 'OK', 'lineId': line.id, 'newAfterId': None})
        else:
            # We're all the way to the bottom!
            swap_with = Line.objects.filter(page=line.page, chapter__number=line.chapter.number,
                                            order=old_order - 1).first()  # type: Line

            return JsonResponse({'Result': 'OK', 'lineId': line.id, 'newAfterId': swap_with.id})

    line.order = new_order
    swap_with.order = old_order

    line.save()
    swap_with.save()

    if difference > 0:
        return JsonResponse({'Result': 'OK', 'lineId': line.id, 'newAfterId': swap_with.id})
    else:
        return JsonResponse({'Result': 'OK', 'lineId': swap_with.id, 'newAfterId': line.id})
