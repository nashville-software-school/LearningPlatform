from rest_framework import serializers
from LearningAPI.models import Technology


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'
