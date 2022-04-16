from rest_framework import serializers
from plants.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('plant_id', 'care_guide', 'common_name', 'sci_name', 'price')