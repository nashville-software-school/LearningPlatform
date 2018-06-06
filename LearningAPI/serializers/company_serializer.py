from rest_framework import serializers
from LearningAPI.models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'phone', 'address')