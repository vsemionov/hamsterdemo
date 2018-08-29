from django.db import models


MAX_NAME_SIZE = 128
MAX_TEXT_SIZE = 32*1024


class Notebook(models.Model):
    name = models.CharField(max_length=MAX_NAME_SIZE)

    def __str__(self):
        return self.name


class Note(models.Model):
    notebook = models.ForeignKey(Notebook, models.PROTECT)

    title = models.CharField(max_length=MAX_NAME_SIZE)
    text = models.TextField(max_length=MAX_TEXT_SIZE)

    def __str__(self):
        return self.title
