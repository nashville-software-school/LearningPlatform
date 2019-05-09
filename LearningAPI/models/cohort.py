from django.db import models
from LearningAPI.models import Instructor, InstructorCohort, Student, StudentCohort

# TODO: Eventually will need properties for distinguishing PT vs FT, web dev vs data, etc
class Cohort(models.Model):
    """Represents a full-time or part-time cohort at NSS"""

    name = models.CharField(max_length=55)
    slack_channel = models.CharField(max_length=55, blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    instructors = models.ManyToManyField(Instructor, through="InstructorCohort")
    students = models.ManyToManyField(Student, through="StudentCohort")

    def __str__(self):
        return self.name
