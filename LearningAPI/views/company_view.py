from rest_framework import viewsets
from LearningAPI.serializers import CompanySerializer
from LearningAPI.models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer