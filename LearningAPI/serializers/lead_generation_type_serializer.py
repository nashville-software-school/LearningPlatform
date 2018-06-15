from rest_framework import serializers
from LearningAPI.models import LeadGenerationType


class LeadGenerationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeadGenerationType
        fields = '__all__'