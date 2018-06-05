from django.contrib.auth.models import Lead
from rest_framework import serializers


class LeadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lead
        # TODO: add company_id
        # TODO: add contact_id
        # TODO: lead_generation_type_id
        fields = ('date', 'notes')