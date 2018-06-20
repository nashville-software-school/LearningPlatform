from rest_framework import viewsets
from LearningAPI.serializers import ApplicationStageSerializer
from LearningAPI.models import ApplicationStage


class ApplicationStageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows application stages to be viewed or edited.
    """
    queryset = ApplicationStage.objects.all()
    serializer_class = ApplicationStageSerializer