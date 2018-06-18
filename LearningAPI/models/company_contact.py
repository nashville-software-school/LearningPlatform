from django.db import models


class CompanyContact(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    contact_id = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)
