from apps.clinic.api.serializers import *
from apps.clinic.models import *
from apps.users.api.permissions import (
    IsAssistant,
    IsManager,
    IsOwner,
    IsRecepcionist,
    IsVeterinary,
)
from rest_framework import viewsets
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AnalysisViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve analysis.
    """

    queryset = Analysis.objects.all()
    serializer_class = AnalysisModelSerializer
    permission_classes = [IsVeterinary, IsAuthenticated]


class TreatmentViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve treatments
    """

    queryset = Treatment.objects.all()
    serializer_class = TreatmentModelSerializer
    permission_classes = [IsVeterinary, IsAuthenticated]


class HospitalizationViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve hospitalizations
    """

    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationModelSerializer
    permission_classes = [IsRecepcionist, IsAuthenticated]


class ProprietorViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete proprietors
    """

    queryset = Proprietor.objects.all()
    serializer_class = ProprietorModelSerializer
    permission_classes = [IsRecepcionist, IsAuthenticated]


class DiseaseViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete diseases
    """

    queryset = Disease.objects.all()
    serializer_class = DiseaseModelSerializer
    permission_classes = [IsVeterinary, IsAuthenticated]


class PetViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete pets
    """

    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer
    permission_classes = [IsAuthenticated]


class ReceptionViewSet(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete receptions
    """

    queryset = Reception.objects.all()
    serializer_class = ReceptionModelSerializer
    permission_classes = [IsRecepcionist,IsAuthenticated]
