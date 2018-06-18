from django.db import models
from . import Placement, Technology


class PlacementTechnology(models.Model):
    technology_id = models.ForeignKey(Technology, on_delete=models.DO_NOTHING)
    placement_id = models.ForeignKey(Placement, on_delete=models.DO_NOTHING)
