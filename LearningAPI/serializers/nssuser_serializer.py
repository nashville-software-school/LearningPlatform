from rest_framework import serializers
from LearningAPI.models import NssUser


class NssUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NssUser
        fields = '__all__'
