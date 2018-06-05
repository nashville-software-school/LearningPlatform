from django.db import models
from . import NssUser
# from . import Lead, StatusType


class LeadStatus(models.Model):
    nss_user = models.ForeignKey(NssUser, on_delete=models.DO_NOTHING)
    # lead_id = models.ForeignKey(Lead, on_delete=models.DO_NOTHING)
    # status_type = models.ForeignKey(StatusType, on_delete=models.DO_NOTHING)
    date = models.DateField()
    notes = models.TextField()