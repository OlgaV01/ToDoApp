from django.db import models


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=200)


class Todo(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
