from rest_framework import viewsets
from LearningAPI.serializers import NssUserExerciseSerializer
from LearningAPI.models import NssUserExercise


class NssUserExerciseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows NSS user-exercise relationships to be viewed or edited.
    """
    queryset = NssUserExercise.objects.all()
    serializer_class = NssUserExerciseSerializer