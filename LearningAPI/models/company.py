from django.db import models
from . import Contact


class Company(models.Model):
    name = models.CharField(max_length=55)
    phone = models.CharField(max_length=55)
    address = models.CharField(max_length=55)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name
