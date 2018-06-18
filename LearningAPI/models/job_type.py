from django.db import models


class JobType(models.Model):
    name = models.CharField(max_length=55)
