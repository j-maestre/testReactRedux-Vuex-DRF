from rest_framework import serializers

from .models import Valoration


class ValorationRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Valoration.objects.all()

    def to_internal_value(self, data):
        valoration, created = Valoration.objects.get_or_create(valoration=data, slug=data.lower())

        return valoration

    def to_representation(self, value):
        return value.valoration
