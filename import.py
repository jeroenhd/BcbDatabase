#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script will import the JSON containing chapter information into the database
"""
import os


try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import json


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BcbDatabase.settings")
    import django
    django.setup()
    from ComicDatabase.models import Chapter

    json_url = "https://www.bittersweetcandybowl.com/app/json/db_main-1.2"

    print("Downloading chapters...")
    response = urlopen(json_url).read().decode("Windows-1252")
    print("Parsing JSON...")
    chapters = json.loads(response)

    print("Importing...")

    for chapterNumber in chapters:
        rawChapter = chapters.get(chapterNumber)
        chapter = Chapter.objects.filter(number=chapterNumber).first()

        if chapter is None:
            chapter = Chapter()
            chapter.number = chapterNumber
            chapter.title = rawChapter.get('title')
            chapter.description = rawChapter.get('description')
            chapter.pageCount = rawChapter['pageCount']
            chapter.save()
            print("Saving new chapter: %s" % chapter)
        else:
            if chapter.pageCount < rawChapter['pageCount']:
                chapter.pageCount = rawChapter.get('pageCount')
                chapter.save()
                print("Updating chapter: %s" % chapter)

    print("Completed")