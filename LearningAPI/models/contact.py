from django.db import models
from . import Company


class Contact(models.Model):
    name = models.CharField(max_length=55)
    phone = models.CharField(max_length=55)
    email = models.EmailField()
    notes = models.TextField()
    companies = models.ManyToManyField(Company)

    def __str__(self):
        return self.name
