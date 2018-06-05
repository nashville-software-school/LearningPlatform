from rest_framework import viewsets
from LearningAPI.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer