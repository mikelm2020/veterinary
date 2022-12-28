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


class AnalysisViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve analysis.
    """

    queryset = Analysis.objects.all()
    serializer_class = AnalysisModelSerializer
    permission_classes = [IsVeterinary]

class TreatmentViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve treatments
    """

    queryset= Treatment.objects.all()
    serializer_class = TreatmentModelSerializer
    permission_classes = [IsVeterinary]

    