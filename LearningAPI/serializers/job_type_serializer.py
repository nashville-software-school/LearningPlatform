from rest_framework import serializers
from LearningAPI.models import JobType


class JobTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'
