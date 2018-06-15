from rest_framework import viewsets
from LearningAPI.serializers import LeadGenerationTypeSerializer
from LearningAPI.models import LeadGenerationType


class LeadGenerationTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lead generation types to be viewed or edited.
    """
    queryset = LeadGenerationType.objects.all()
    serializer_class = LeadGenerationTypeSerializer