from django.db import models


class Chapter(models.Model):
    """A single chapter"""

    number = models.DecimalField(decimal_places=1, max_digits=4)
    """The chapter number"""

    title = models.TextField(max_length=200)
    """The chapter title"""

    description = models.TextField(max_length=200)
    """The chapter description"""

    pageCount = models.IntegerField()
    """The amount of pages that are in this chapter"""

    def __str__(self):
        """'Chapter 1: Simple Pleasures (6 pages)'"""
        return "Chapter %s: %s (%s pages)" % (self.number, self.title, self.pageCount)


class Species(models.Model):
    """A single species (think cat, dog)"""

    name = models.TextField(max_length=200)
    """The name of the species"""

    def __str__(self):
        """'cat'"""
        return self.name


class Character(models.Model):
    """A character in the comic"""

    name = models.TextField(max_length=200)
    """The name of the character"""

    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    """The species of the character"""

    def __str__(self):
        """'Lucy (cat)'"""
        return "%s (%s)" % (self.name, self.species)


class Line(models.Model):
    """A line, said by a character on a page"""

    class Meta:
        unique_together = (('chapter', 'page', 'order'),)

    text = models.TextField(max_length=500)
    """The text of the line"""

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    """The character saying the line"""

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    """The chapter this line is in"""

    page = models.IntegerField()
    """The page this line is on"""

    order = models.IntegerField(default=0)
    """An ordering integer so that the lines can be re-ordered"""

    def __str__(self):
        """'[1:1] <Radio> Welcome to a lovely sunny Saturday, America! [...]'"""
        return "[%s/%s:%s] <%s> %s" % (self.chapter.number, self.page, self.order, self.character, self.text)
