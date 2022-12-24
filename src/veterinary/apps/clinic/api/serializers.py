from rest_framework import serializers
from apps.clinic.models import *

class AnalysisModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = (
            "name",
            "description",
            "price",
        )

class TreatmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = (
            "name",
            "description",
            "treatment_type",
            "price",
            "period",
        )

