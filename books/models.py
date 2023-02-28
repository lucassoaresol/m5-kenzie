from django.db import models
import uuid


class Book(models.Model):
    pages = models.IntegerField()
    title = models.CharField(max_length=255)
    author = models.ForeignKey("books.Author", on_delete=models.CASCADE)


class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
