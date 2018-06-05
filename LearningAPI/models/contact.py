from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=55)
    phone = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    notes = models.TextField()