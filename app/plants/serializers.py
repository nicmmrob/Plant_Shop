from rest_framework import serializers
from plants.models import Plants


class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plants
        fields = ('plant_id', 'care_guide', 'common_name', 'sci_name', 'price')