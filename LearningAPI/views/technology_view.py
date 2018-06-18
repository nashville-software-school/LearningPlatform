from rest_framework import viewsets
from LearningAPI.serializers import TechnologySerializer
from LearningAPI.models import Technology


class TechnologyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows technologies to be viewed or edited.
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
