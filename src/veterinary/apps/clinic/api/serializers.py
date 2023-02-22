from apps.clinic.models import *
from rest_framework import serializers
from apps.users.models import User


class AnalysisModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = (
            "id",
            "name",
            "description",
            "price",
        )


class TreatmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = (
            "id",
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
            "id",
            "hospitalization_type",
            "price",
        )


class ProprietorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietor
        fields = (
            "id",
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
            "id",
            "name",
            "description",
            "mandatory_declaration",
        )


class PetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            "id",
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
            "id",
            "register_date",
            "reason",
            "condition",
            "pet",
        )


class DisplacementModelSerializer(serializers.ModelSerializer):
    reception = serializers.PrimaryKeyRelatedField(queryset=Reception.objects.all())
    assistant = serializers.ReadOnlyField(source="assistant.username")

    class Meta:
        model = Displacement
        fields = (
            "id",
            "displacement_date",
            "price",
            "alternate_address",
            "reception",
            "assistant",
        )


class AssistantSerializer(serializers.ModelSerializer):
    assistant_perform = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.assistants()
    )

    class Meta:
        model = User
        fields = ("id", "username", "assistant_perform")


class DiagnosticModelSerializer(serializers.ModelSerializer):
    reception = serializers.PrimaryKeyRelatedField(queryset=Reception.objects.all())
    analysis = serializers.PrimaryKeyRelatedField(queryset=Analysis.objects.all())

    class Meta:
        model = Diagnostic
        fields = (
            "id",
            "diagnostic_date",
            "result",
            "reception",
            "analysis",
        )


class TreatmentAppliedModelSerializer(serializers.ModelSerializer):
    reception = serializers.PrimaryKeyRelatedField(queryset=Reception.objects.all())
    veterinary = serializers.ReadOnlyField(source="veterinary.username")

    class Meta:
        model = TreatmentApplied
        fields = (
            "id",
            "treatment_applied_type",
            "treatment_applied_date",
            "observation",
            "reception",
            "veterinary",
        )


class VeterinarySerializer(serializers.ModelSerializer):
    veterinary_perform = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.veterinaries()
    )

    class Meta:
        model = User
        fields = ("id", "username", "veterinary_perform")


class MandatoryTreatmentModelSerializer(serializers.ModelSerializer):
    treatment_applied = serializers.PrimaryKeyRelatedField(
        queryset=TreatmentApplied.objects.all()
    )
    treatment = serializers.PrimaryKeyRelatedField(queryset=Treatment.objects.all())

    class Meta:
        model = MandatoryTreatment
        fields = (
            "id",
            "treatment_applied",
            "treatment",
            "drug",
            "drug_serial",
        )


class OptionalTreatmentModelSerializer(serializers.ModelSerializer):
    treatment_applied = serializers.PrimaryKeyRelatedField(
        queryset=TreatmentApplied.objects.all()
    )
    treatment = serializers.PrimaryKeyRelatedField(queryset=Treatment.objects.all())

    class Meta:
        model = OptionalTreatment
        fields = (
            "id",
            "treatment_applied",
            "treatment",
        )


class InternshipModelSerializer(serializers.ModelSerializer):
    reception = serializers.PrimaryKeyRelatedField(queryset=Reception.objects.all())
    hospitalization = serializers.PrimaryKeyRelatedField(
        queryset=Hospitalization.objects.all()
    )

    class Meta:
        model = Internship
        fields = (
            "id",
            "reception",
            "hospitalization",
            "initial_date",
            "final_date",
            "room",
        )


class DiscoverDiseaseModelSerializer(serializers.ModelSerializer):
    diagnostic = serializers.PrimaryKeyRelatedField(queryset=Diagnostic.objects.all())
    disease = serializers.PrimaryKeyRelatedField(queryset=Disease.objects.all())

    class Meta:
        model = DicoverDisease
        fields = (
            "id",
            "diagnostic",
            "disease",
        )


class InvoiceModelSerializer(serializers.ModelSerializer):
    reception = serializers.PrimaryKeyRelatedField(queryset=Reception.objects.all())

    class Meta:
        model = Invoice
        fields = (
            "id",
            "emission_date",
            "invoice_type",
            "pay_date",
            "total",
            "reception",
        )
