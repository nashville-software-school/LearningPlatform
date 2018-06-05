from rest_framework import serializers
from LearningAPI.models import Lead


class LeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lead
        # TODO: add company_id
        # TODO: add contact_id
        # TODO: lead_generation_type_id
        fields = ('date', 'notes')