from rest_framework import serializers
from LearningAPI.models import ApplicationStage


class ApplicationStageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationStage
        fields = '__all__'
