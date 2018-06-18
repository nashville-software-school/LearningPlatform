from rest_framework import serializers
from LearningAPI.models import CompanyContact


class CompanyContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyContact
        fields = '__all__'
