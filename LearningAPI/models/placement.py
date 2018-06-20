from django.db import models
from . import NssUser, JobType, Company, Technology


class Placement(models.Model):
    nss_user_id = models.ForeignKey(NssUser, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    job_type_id = models.ForeignKey(JobType, on_delete=models.DO_NOTHING)
    salary = models.IntegerField()
    start_date = models.DateField()
    technologies = models.ManyToManyField(Technology)
