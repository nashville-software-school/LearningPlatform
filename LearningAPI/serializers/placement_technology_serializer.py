from rest_framework import serializers
from LearningAPI.models import PlacementTechnology


class PlacementTechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlacementTechnology
        fields = '__all__'
