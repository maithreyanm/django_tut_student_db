from django.db import models

# Create your models here.
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)



class Email(models.Model):
    email_1 = models.EmailField()
    email_2 = models.EmailField()