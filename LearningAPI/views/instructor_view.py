from rest_framework import viewsets
from LearningAPI.models import Instructor
from LearningAPI.serializers import InstructorSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that automagically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions.
    """
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
