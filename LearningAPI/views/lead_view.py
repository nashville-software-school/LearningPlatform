from rest_framework import viewsets
from LearningAPI.serializers import LeadSerializer
from django.contrib.auth.models import Lead


class LeadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows leads to be viewed or edited.
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer