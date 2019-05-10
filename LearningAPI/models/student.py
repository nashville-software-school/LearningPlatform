from django.db import models
from django.core.validators import RegexValidator
from . import CommonProps

class Student(CommonProps):
    """Represents an NSS student for any type of cohort"""

    # regex should match the following: (555) 444-6789, 555-444-6789, 555.444.6789, 555 444 6789
    phone_regex = RegexValidator(regex=r'\(?\d+\)?[-.\s]?\d+[-.\s]?\d+')

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    student_number = models.PositiveIntegerField()

    @property
    def full_name(self):
        try:
          current_cohort = self.current_cohort
        except AttributeError:
          current_cohort = ''
        return f"{self.first_name} {self.last_name}{':'} {current_cohort}"

    class Meta:
      ordering = ['student_number']
