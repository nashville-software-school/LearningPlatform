from django.db import models


class Cohort(models.Model):
    name = models.CharField(max_length=55)
    slack_channel = models.CharField(max_length=55, blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.name
