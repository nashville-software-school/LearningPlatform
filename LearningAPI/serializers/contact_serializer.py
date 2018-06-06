from rest_framework import serializers
from LearningAPI.models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'notes')