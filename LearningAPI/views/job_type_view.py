from rest_framework import viewsets
from LearningAPI.serializers import JobTypeSerializer
from LearningAPI.models import JobType


class JobTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows job types to be viewed or edited.
    """
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer
