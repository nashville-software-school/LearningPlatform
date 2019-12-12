import datetime
from django.db import models

class CommonProps(models.Model):
    """An abstract class for sharing common properties across multiple other classes"""

    @property
    def current_cohort(self):
        # Find the student's cohort with the most recent timestamp. Chain .last() to pull out the instance object that represents the date that's farthest away.
        cohort = self.cohorts.all().order_by('date_assigned').last().cohort
        print("cohort?", cohort)
        if not cohort:
          return None
        return cohort

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True
