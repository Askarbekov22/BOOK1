from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')
