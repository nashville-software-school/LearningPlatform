from django.db import models


class Cohort(models.Model):
    name = models.CharField(max_length=55)
    slack_channel = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name