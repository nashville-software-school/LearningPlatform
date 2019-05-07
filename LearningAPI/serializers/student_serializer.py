from rest_framework import serializers
from LearningAPI.models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Student
      fields = '__all__'
