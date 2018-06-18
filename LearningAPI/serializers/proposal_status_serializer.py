from rest_framework import serializers
from LearningAPI.models import ProposalStatus


class ProposalStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProposalStatus
        fields = '__all__'
