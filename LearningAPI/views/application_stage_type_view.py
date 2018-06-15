from rest_framework import viewsets
from LearningAPI.serializers import ApplicationStageTypeSerializer
from LearningAPI.models import ApplicationStageType


class ApplicationStageTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows application stage types to be viewed or edited.
    """
    queryset = ApplicationStageType.objects.all()
    serializer_class = ApplicationStageTypeSerializer
