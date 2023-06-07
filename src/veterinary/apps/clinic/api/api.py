from apps.clinic.api.serializers import *
from apps.clinic.models import *
from apps.clinic.pagination import ExtendedPagination
from apps.users.api.permissions import (
    IsAssistant,
    IsManager,
    IsRecepcionist,
    IsVeterinary,
)
from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from knox.auth import TokenAuthentication
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class AnalysisViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve analysis.
    """

    queryset = Analysis.objects.all()
    serializer_class = AnalysisModelSerializer
    permission_classes = [IsVeterinary]
    pagination_class = ExtendedPagination


class TreatmentViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve treatments
    """

    queryset = Treatment.objects.all()
    serializer_class = TreatmentModelSerializer
    permission_classes = [IsVeterinary | IsManager]
    pagination_class = ExtendedPagination


class HospitalizationViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve hospitalizations
    """

    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationModelSerializer
    permission_classes = [IsRecepcionist | IsManager]
    pagination_class = ExtendedPagination


class ProprietorViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete proprietors
    """

    queryset = Proprietor.objects.all()
    serializer_class = ProprietorModelSerializer
    permission_classes = [IsRecepcionist]
    pagination_class = ExtendedPagination


class DiseaseViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete diseases
    """

    queryset = Disease.objects.all()
    serializer_class = DiseaseModelSerializer
    permission_classes = [IsVeterinary]
    pagination_class = ExtendedPagination


class PetViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete pets
    """

    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer
    permission_classes = [IsManager | IsVeterinary | IsRecepcionist]
    pagination_class = ExtendedPagination


class ReceptionViewSet(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete receptions
    """

    queryset = Reception.objects.all()
    serializer_class = ReceptionModelSerializer
    permission_classes = [IsRecepcionist | IsAssistant | IsVeterinary | IsManager]
    pagination_class = ExtendedPagination


class DisplacementViewSet(viewsets.GenericViewSet):
    """
    List, create, update and retrieve diplacements
    """

    serializer_class = DisplacementModelSerializer
    list_serializer_class = ListDisplacementModelSerializer
    pagination_class = ExtendedPagination
    permission_classes = [IsAssistant | IsManager]

    def get_queryset(self, pk=None):
        if pk is None:
            return Displacement.objects.filter(assistant=self.request.user)
        else:
            return Displacement.objects.filter(
                id=pk, assistant=self.request.user
            ).first()

    def get_object(self, pk):
        return get_object_or_404(Displacement, pk=pk)

    def list(self, request, *args, **kwargs):
        """
        Get a collection of displacements
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def create(self, request):
        """
        Create a displacement
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(assistant=self.request.user)

            return Response(
                {"message": "desplazamiento registrado correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Hay errores en el registro", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=OpenApiTypes.INT, location=OpenApiParameter.PATH
            ),
        ],
    )
    def retrieve(self, request, pk=None):
        """
        Get a displacement
        """
        displacement = self.get_object(pk)
        displacement_serializer = self.list_serializer_class(displacement)
        return Response(displacement_serializer.data)


class DiagnosticViewSet(viewsets.GenericViewSet):
    """
    List, create, update and retrieve diagnostics
    """

    serializer_class = DiagnosticModelSerializer
    list_serializer_class = ListDiagnosticModelSerializer
    pagination_class = ExtendedPagination
    permission_classes = [IsVeterinary | IsManager]

    def get_queryset(self, pk=None):
        if pk is None:
            return Diagnostic.objects.all()
        else:
            return Diagnostic.objects.filter(id=pk).first()

    def get_object(self, pk):
        return get_object_or_404(Diagnostic, pk=pk)

    def list(self, request, *args, **kwargs):
        """
        Get a collection of diagnostics
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def create(self, request):
        """
        Create a diagnostic
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "diagnóstico registrado correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Hay errores en el registro", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=OpenApiTypes.INT, location=OpenApiParameter.PATH
            ),
        ],
    )
    def retrieve(self, request, pk=None):
        """
        Get a diagnostic
        """
        diagnostic = self.get_object(pk)
        diagnostic_serializer = self.list_serializer_class(diagnostic)
        return Response(diagnostic_serializer.data)


class TreatmentAppliedViewSet(viewsets.GenericViewSet):
    """
    List, create, update and retrieve treatments applied
    """

    serializer_class = TreatmentAppliedModelSerializer
    list_serializer_class = ListTreatmentAppliedModelSerializer
    pagination_class = ExtendedPagination
    permission_classes = [IsVeterinary | IsManager]

    def get_queryset(self, pk=None):
        if pk is None:
            return TreatmentApplied.objects.filter(veterinary=self.request.user)
        else:
            return TreatmentApplied.objects.filter(
                id=pk, veterinary=self.request.user
            ).first()

    def get_object(self, pk):
        return get_object_or_404(TreatmentApplied, pk=pk)

    def list(self, request, *args, **kwargs):
        """
        Get a collection of treatments applied
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def create(self, request):
        """
        Create a treatment applied
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(veterinary=self.request.user)

            return Response(
                {"message": "tratamiento aplicado registrado correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Hay errores en el registro", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=OpenApiTypes.INT, location=OpenApiParameter.PATH
            ),
        ],
    )
    def retrieve(self, request, pk=None):
        """
        Get a treatment applied
        """
        treatment_applied = self.get_object(pk)
        treatment_applied_serializer = self.list_serializer_class(treatment_applied)
        return Response(treatment_applied_serializer.data)

# class MandatoryTreatmentViewSet(viewsets.ModelViewSet):

#     queryset = MandatoryTreatment.objects.all()
#     serializer_class = MandatoryTreatmentModelSerializer
#     pagination_class = ExtendedPagination
#     permission_classes = [IsVeterinary | IsManager]

class MandatoryTreatmentViewSet(viewsets.GenericViewSet):
    """
    List, create, update and retrieve mandatory treatments
    """

    serializer_class = MandatoryTreatmentModelSerializer
    list_serializer_class = ListMandatoryTreatmentModelSerializer
    pagination_class = ExtendedPagination
    permission_classes = [IsVeterinary | IsManager]

    def get_queryset(self, pk=None):
        if pk is None:
            return MandatoryTreatment.objects.all()
        else:
            return MandatoryTreatment.objects.filter(
                id=pk
            ).first()

    def get_object(self, pk):
        return get_object_or_404(MandatoryTreatment, pk=pk)

    def list(self, request, *args, **kwargs):
        """
        Get a collection of mandatory treatments
        """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.list_serializer_class(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def create(self, request):
        """
        Create a mandatory treatment
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "tratamiento obligatorio registrado correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Hay errores en el registro", "error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=OpenApiTypes.INT, location=OpenApiParameter.PATH
            ),
        ],
    )
    def retrieve(self, request, pk=None):
        """
        Get a mandatory treatment
        """
        mandatory_treatment = self.get_object(pk)
        mandatory_treatment_serializer = self.list_serializer_class(mandatory_treatment)
        return Response(mandatory_treatment_serializer.data)
