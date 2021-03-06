from django.db import models
from django.utils import timezone

# No need to import the referenced models, thanks to 'lazy loading' that happens when we put the Model name in quotes. This helps avoid circular import error
class StudentCohort(models.Model):
    """Represents relationship between and Student and Cohort"""

    student = models.ForeignKey("Student", on_delete=models.DO_NOTHING, related_name="cohorts")
    cohort = models.ForeignKey("Cohort", on_delete=models.DO_NOTHING)
    date_assigned = models.DateField(default=timezone.now, editable=False)
