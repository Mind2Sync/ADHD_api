from rest_framework import serializers
from .models import MRIPrediction

class MRIPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MRIPrediction
        fields = ["name", "age", "sex", "country", "mriScan"]


class PredictionSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = MRIPrediction
        fields =["name",'age',"sex","country","mriScan","prediction", "adhdType"]
