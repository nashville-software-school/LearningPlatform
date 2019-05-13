from django.db import models
# import model(s) from nss_users_api app
from LearningAPI.models import Instructor, Student, CohortType

class ReasonCode(models.Model):
    '''
    Reason for Withdrawal
    '''
    thec_code = models.PositiveIntegerField()
    title = models.CharField(max_length=50)

    def __str__(self):
      return self.title

class DisengagementType(models.Model):
    '''
    Withdrawal or Leave of Absence
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
      return self.name

class StudentDisengagement(models.Model):
    disengagement_type = models.ForeignKey(DisengagementType, null=True, on_delete=models.SET_NULL)
    disengagement_detail = models.TextField(blank=True, null=True, default="")
    # THEC definitions
    reason = models.ForeignKey(ReasonCode, blank=True, null=True, on_delete=models.SET_NULL)
    # Is CASCADE the correct thing to do here?
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    effective_date = models.DateField(blank=True)
    last_attendance_date = models.DateField(blank=True)
    intended_return_date = models.DateField(blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    cohort_type = models.ForeignKey(CohortType, null=True, on_delete=models.SET_NULL)
    return_conditions = models.TextField(blank=True, null=True)
    # Don't need upload_to because we set MEDIA_ROOT in settings.py
    pdf = models.FileField(null=True, blank=True)
    pdf_slug = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        unique_together = ["student", "effective_date"]


class StudentNote(models.Model):
    '''
    A record of an instructor's concerns about a student
    '''
    note = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
