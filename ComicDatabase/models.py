from django.db import models


class Chapter(models.Model):
    """A single chapter"""
    number = models.DecimalField(decimal_places=1, max_digits=4)
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    pageCount = models.IntegerField()


class Species(models.Model):
    """A single species (think cat, dog)"""
    name = models.TextField(max_length=200)


class Character(models.Model):
    """A character in the comic"""
    name = models.TextField(max_length=200)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)


class Line(models.Model):
    """A line, said by a character on a page"""
    text = models.TextField(max_length=500)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    page = models.IntegerField()
