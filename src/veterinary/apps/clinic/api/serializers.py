from apps.clinic.models import *
from rest_framework import serializers
from apps.users.models import User

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


class HospitalizationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospitalization
        fields = (
            "hospitalization_type",
            "price",
        )


class ProprietorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietor
        fields = (
            "name",
            "last_name",
            "address",
            "phone",
            "email",
        )


class DiseaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = (
            "name",
            "description",
            "mandatory_declaration",
        )


class PetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            "name",
            "kind",
            "breed",
            "sex",
            "birth_date",
            "death_date",
            "proprietor",
        )


class ReceptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = (
            "register_date",
            "reason",
            "condition",
            "pet",
        )


class DisplacementModelSerializer(serializers.ModelSerializer):
    reception = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="reception-detail"
    )
    assistant = serializers.ReadOnlyField(source="assistant.username")


    class Meta:
        model = Displacement
        fields = (
            "displacement_date",
            "price",
            "alternate_address",
            "reception",
            "assistant",
        )

class AssistantSerializer(serializers.ModelSerializer):
    assistant_perform = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.assistants())

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "assistant_perform"
        )

class DiagnosticModelSerializer(serializers.ModelSerializer):
    reception = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="reception-detail"
    )
    analysis = serializers.HyperlinkedRelatedField(
        many= True, read_only=True, view_name="analysis-detail"
    )

    class Meta:
        model = Diagnostic
        fields = (
            "diagnostic_date",
            "result",
            "reception",
            "analysis",
        )

class TreatmentAppliedModelSerializer(serializers.ModelSerializer):
    reception = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="reception-detail"
    )
    veterinary = serializers.ReadOnlyField(source="veterinary.username")

    class Meta:
        model= TreatmentApplied
        fields = (
            "treatment_applied_type",
            "treatment_applied_date",
            "observation",
            "reception",
            "veterinary"
        )

class VeterinarySerializer(serializers.ModelSerializer):
    veterinary_perform = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.veterinaries())

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "veterinary_perform"
        )

class MandatoryTreatmentModelSerializer(serializers.ModelSerializer):
    treatment_applied = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="treatment_applied-detail"
    )
    treatment = serializers.HyperlinkedRelatedField(
        many=True, read_only= True, view_name="treatment-detail"
    )

    class Meta:
        model = MandatoryTreatment
        fields = (
            "treatment_applied",
            "treatment",
            "drug",
            "drug_serial",
        )

class OptionalTreatmentModelSerializer(serializers.ModelSerializer):
    treatment_applied = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name="treatment_applied-detail"
    )
    treatment = serializers.HyperlinkedRelatedField(
        many=True, read_only= True, view_name="treatment-detail"
    )

    class Meta:
        model = OptionalTreatment
        fields = (
            "treatment_applied",
            "treatment",
        )

class InternshipModelSerializer(serializers.ModelSerializer):
    reception = serializers.HyperlinkedRelatedField(
        many=False, read_only= True, view_name="recéption-detail"
    )
    hospitalization = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="hospitalization-detail"
    )

    class Meta:
        model = Internship
        fields= (
            "reception",
            "hospitalization",
            "initial_date",
            "final_date",
            "room",
        )

class DiscoverDiseaseModelSerializer(serializers.ModelSerializer):
    diagnostic = serializers.HyperlinkedRelatedField(
        many=False, read_only= True, view_name="diagnostic-detail"
    )
    disease = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="disease-detail"
    )
    class Meta:
        model = DicoverDisease
        fields = (
            "diagnostic",
            "disease",
        )

class InvoiceModelSerializer(serializers.ModelSerializer):
    reception = serializers.HyperlinkedRelatedField(
        many=False, read_only= True, view_name="recéption-detail"
    )
    class Meta:
        model = Invoice
        fields = (
            "emission_date",
            "invoice_type",
            "pay_date",
            "total",
            "reception",
        )
        