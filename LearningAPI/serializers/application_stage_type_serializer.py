from rest_framework import serializers
from LearningAPI.models import ApplicationStageType


class ApplicationStageTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationStageType
        fields = '__all__'
