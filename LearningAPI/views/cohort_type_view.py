from rest_framework import viewsets
from LearningAPI.serializers import CohortTypeSerializer
from LearningAPI.models import CohortType


class CohortTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Cohort types to be viewed or edited.
    """
    queryset = CohortType.objects.all()
    serializer_class = CohortTypeSerializer
