from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class BookCopy(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name="authors")
    title = models.CharField(max_length=100)
    year = models.IntegerField()
