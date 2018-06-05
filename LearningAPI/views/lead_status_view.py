from rest_framework import viewsets
from LearningAPI.serializers import LeadStatusSerializer
from LearningAPI.models import LeadStatus


class LeadStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lead statuses to be viewed or edited.
    """
    queryset = LeadStatus.objects.all()
    serializer_class = LeadStatusSerializer