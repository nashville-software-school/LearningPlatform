from rest_framework import serializers
from LearningAPI.models import Placement


class PlacementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Placement
        fields = '__all__'
