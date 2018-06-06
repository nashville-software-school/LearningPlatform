from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=55)
    phone = models.CharField(max_length=55)
    address = models.CharField(max_length=55)