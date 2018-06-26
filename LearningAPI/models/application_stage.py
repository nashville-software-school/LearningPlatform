from django.db import models
from . import NssUser, ApplicationStageType, Contact, Company, LeadGenerationType


class ApplicationStage(models.Model):
    nss_user = models.ForeignKey(NssUser, on_delete=models.DO_NOTHING)
    application_stage_type = models.ForeignKey(ApplicationStageType, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    lead_generation_type = models.ForeignKey(LeadGenerationType, on_delete=models.DO_NOTHING)
    date = models.DateField()
    notes = models.CharField(max_length=55)

    def __str__(self):
        return self.name
