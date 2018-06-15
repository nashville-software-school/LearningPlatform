from django.db import models
from . import Company, Contact, LeadGenerationType


class Lead(models.Model):
    date = models.DateField(max_length=55)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)
    contact_id = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, null=True)
    notes = models.TextField()
    # default: 5 = Other
    lead_generation_type_id = models.ForeignKey(LeadGenerationType, on_delete=models.DO_NOTHING, default=5)