from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=55)