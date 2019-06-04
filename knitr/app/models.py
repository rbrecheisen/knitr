from django.db import models


class Document(models.Model):
    id = models.IntegerField(name='id', primary_key=True)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=1024)
