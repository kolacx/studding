from django.db import models
from django.db.models import SET_DEFAULT, SET_NULL


class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    position = models.ForeignKey('Position', on_delete=SET_NULL, null=True)
    departament = models.ForeignKey('Departament', on_delete=SET_NULL, null=True)


class Position(models.Model):
    title = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    departament = models.ForeignKey('Departament', on_delete=SET_NULL, null=True)


class Departament(models.Model):
    title = models.CharField(max_length=128)
    workers = models.ManyToManyField('User', related_name='workers')
