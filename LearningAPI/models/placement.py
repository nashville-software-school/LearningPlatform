from django.db import models


class Placement(models.Model):
    nss_user_id = models.ForeignKey(NssUser, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    job_type_id = models.ForeignKey(JobType, on_delete=models.DO_NOTHING)
    salary = models.CharField(max_length=55)
    start_date = models.DateField(max_length=55)
