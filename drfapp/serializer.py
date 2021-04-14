from rest_framework import serializers
from drfapp.models import DrfModel


class DrfModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    age = serializers.IntegerField()

    class Meta:
        model = DrfModel
        fields = '__all__'