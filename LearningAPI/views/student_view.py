from rest_framework import viewsets
from LearningAPI.serializers import StudentSerializer
from LearningAPI.models import Student

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that automagically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
