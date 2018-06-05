from rest_framework import serializers
from LearningAPI.models import LeadStatus


class LeadStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeadStatus
        fields = '__all__'