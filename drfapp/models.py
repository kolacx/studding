from django.db import models


class DrfModel(models.Model):
    name = models.CharField(max_length=123)
    age = models.IntegerField()
    is_gey = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
