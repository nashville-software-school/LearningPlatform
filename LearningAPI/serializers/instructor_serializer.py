from rest_framework import serializers
from LearningAPI.models import Instructor


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
      model = Instructor
      fields = '__all__'
