from rest_framework import serializers
from LearningAPI.models import UserCohort


class UserCohortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCohort
        fields = '__all__'