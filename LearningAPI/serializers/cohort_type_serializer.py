from rest_framework import serializers
from LearningAPI.models import CohortType


class CohortTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CohortType
        fields = '__all__'
