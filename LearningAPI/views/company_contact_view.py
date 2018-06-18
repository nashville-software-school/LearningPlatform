from rest_framework import viewsets
from LearningAPI.serializers import CompanyContactSerializer
from LearningAPI.models import CompanyContact


class CompanyContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CompanyContact.objects.all()
    serializer_class = CompanyContactSerializer
