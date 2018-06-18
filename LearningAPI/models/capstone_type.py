from django.db import models

class CapstoneType(models.Model):
    type = models.CharField(max_length=55)

    def __str__(self):
        return self.type
