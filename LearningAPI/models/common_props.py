import datetime
from django.db import models

class CommonProps(models.Model):
    """An abstract class for sharing common properties across multiple other classes"""

    @property
    def current_cohort(self):
        # Find the cohort with an end date after today. Chain .last() to pull out the instance object that represents the date that's farthest away.
        cohort = self.cohort_set.filter(end_date__gt=datetime.datetime.now().date()).order_by('end_date').last()
        if not cohort:
          return None
        return cohort

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True
