import datetime
from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    """Represents any lead instructor or junior instructor at NSS"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO: default doesn't seem to work in sqlite. Maybe in another SQL dialect?
    is_awesome = models.BooleanField(default=True)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def current_cohort(self):
        try:
          cohort = self.cohort_set.filter(end_date__gt=datetime.datetime.now().date())
          print('cohort?', cohort)
        except model.DoesNotExist:
          cohort = None
        return cohort

    def __str__(self):
        return self.full_name
