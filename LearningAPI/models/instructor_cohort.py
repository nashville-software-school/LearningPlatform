from django.db import models
from . import Instructor, Cohort

class InstructorCohort(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    cohort = models.ForeignKey(Cohort, on_delete=models.DO_NOTHING)
