from rest_framework import viewsets
from LearningAPI.serializers import PlacementTechnologySerializer
from LearningAPI.models import PlacementTechnology


class PlacementTechnologyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows placement-technology relationships to be viewed or edited.
    """
    queryset = PlacementTechnology.objects.all()
    serializer_class = PlacementTechnologySerializer