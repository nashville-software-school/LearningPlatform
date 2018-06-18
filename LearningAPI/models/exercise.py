from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
