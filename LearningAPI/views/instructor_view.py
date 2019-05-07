from rest_framework import viewsets
from LearningAPI.serializers import InstructorSerializer
from LearningAPI.models import Instructor

class InstructorViewSet(viewsets.ModelViewSet):
    """
    This viewset automagically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions.
    """
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
