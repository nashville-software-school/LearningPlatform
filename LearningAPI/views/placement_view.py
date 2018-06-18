from rest_framework import viewsets
from LearningAPI.serializers import PlacementSerializer
from LearningAPI.models import Placement


class PlacementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows placements to be viewed or edited.
    """
    queryset = Placement.objects.all()
    serializer_class = PlacementSerializer
