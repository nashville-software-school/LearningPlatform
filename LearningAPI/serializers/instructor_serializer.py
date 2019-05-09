from rest_framework import serializers
from LearningAPI.models import Instructor


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    current_cohort = serializers.ReadOnlyField()

    class Meta:
      model = Instructor
      exclude = ('user',)
