from django.db import models
from . import NssUser, ApplicationStageType, Contact, Company, LeadGenerationType


class ApplicationStage(models.Model):
    nss_user_id = models.ForeignKey(NssUser, on_delete=models.DO_NOTHING)
    application_stage_type_id = models.ForeignKey(ApplicationStageType, on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    contact_id = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
    lead_generation_type_id = models.ForeignKey(LeadGenerationType, on_delete=models.DO_NOTHING)
    date = models.DateField()
    notes = models.CharField(max_length=55)

    def __str__(self):
        return self.name
