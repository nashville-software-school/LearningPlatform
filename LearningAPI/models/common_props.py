import datetime
from django.db import models

class CommonProps(models.Model):
    """An abstract class for sharing common properties across multiple other classes"""

    @property
    def current_cohort(self):
        try:
          # Find the cohort with an end date after today. Chain .first() to pull out the instance object
          cohort = self.cohort_set.filter(end_date__gt=datetime.datetime.now().date()).first()
          print("CUREEEEEENT", cohort)
        except model.DoesNotExist:
          cohort = None
        return cohort.name

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True
