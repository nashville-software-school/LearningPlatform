from django.db import models
from . import NssUser, JobType, Company, Technology


class Placement(models.Model):
    nss_user = models.ForeignKey(NssUser, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    job_type = models.ForeignKey(JobType, on_delete=models.DO_NOTHING)
    salary = models.IntegerField()
    start_date = models.DateField()
    technologies = models.ManyToManyField(Technology)
