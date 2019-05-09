from django.db import models

# No need to import the referenced models, thanks to 'lazy loading' that happens when we put the Model name in quotes. This helps avoid circular import error
class InstructorCohort(models.Model):
    """Represents relationship between and Instructor and Cohort"""

    instructor = models.ForeignKey("Instructor", on_delete=models.DO_NOTHING)
    cohort = models.ForeignKey("Cohort", on_delete=models.DO_NOTHING)
