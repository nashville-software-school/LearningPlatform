from django.db import models


class LeadGenerationType(models.Model):
    name = models.CharField(max_length=55)