from apps.clinic.api.serializers import *
from apps.clinic.models import *
from apps.users.api.permissions import (
    IsAssistant,
    IsManager,
    IsRecepcionist,
    IsVeterinary,
)
from django.shortcuts import get_object_or_404
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


class TreatmentViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve treatments
    """

    queryset = Treatment.objects.all()
    serializer_class = TreatmentModelSerializer
    permission_classes = [IsVeterinary | IsManager]


class HospitalizationViewset(viewsets.ReadOnlyModelViewSet):
    """
    List and retrieve hospitalizations
    """

    queryset = Hospitalization.objects.all()
    serializer_class = HospitalizationModelSerializer
    permission_classes = [IsRecepcionist | IsManager]


class ProprietorViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete proprietors
    """

    queryset = Proprietor.objects.all()
    serializer_class = ProprietorModelSerializer
    permission_classes = [IsRecepcionist]


class DiseaseViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete diseases
    """

    queryset = Disease.objects.all()
    serializer_class = DiseaseModelSerializer
    permission_classes = [IsVeterinary]


class PetViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete pets
    """

    queryset = Pet.objects.all()
    serializer_class = PetModelSerializer
    permission_classes = [IsManager | IsVeterinary | IsRecepcionist]


class ReceptionViewSet(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete receptions
    """

    queryset = Reception.objects.all()
    serializer_class = ReceptionModelSerializer
    permission_classes = [IsRecepcionist | IsAssistant | IsVeterinary]


# class DisplacementViewSet(viewsets.ModelViewSet):
#     """
#     List, create, update, retrieve and delete displacements
#     """

#     queryset = Displacement.objects.all()
#     serializer_class = DisplacementModelSerializer
#     permission_classes = [IsRecepcionist | IsAssistant | IsVeterinary]


class DisplacementViewSet(viewsets.GenericViewSet):

    """
    List, create, update, retrieve and delete diplacements
    """

    serializer_class = DisplacementModelSerializer
    list_serializer_class = ListDisplacementModelSerializer

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
            serializer = self.list_serializer_class(page, many=True)
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

    # @extend_schema(
    #     parameters=[
    #         OpenApiParameter(
    #             name="id", type=OpenApiTypes.INT, location=OpenApiParameter.PATH
    #         ),
    #     ],
    # )
    def retrieve(self, request, pk=None):
        """
        Get a displacement
        """
        displacement = self.get_object(pk)
        displacement_serializer = self.list_serializer_class(displacement)
        return Response(displacement_serializer.data)

    # @extend_schema(
    #     parameters=[
    #         OpenApiParameter(
    #             name="id", type=OpenApiTypes.INT, location=OpenApiParameter.PATH
    #         ),
    #     ],
    # )
    def destroy(self, request, pk=None):
        """
        Delete a displacement in logical mode
        """
        displacement_destroy = self.serializer_class.Meta.model.objects.filter(
            id=pk
        ).update(state=False)
        if displacement_destroy == 1:
            return Response(
                {"message": "desplazamiento eliminada correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "No existe el desplazamiento que desea eliminar"},
            status=status.HTTP_404_NOT_FOUND,
        )

    # def perform_create(self, serializer):
    #     serializer.save(assistant=self.request.user)


class DiagnosticViewset(viewsets.ModelViewSet):
    """
    List, create, update, retrieve and delete diagnostics
    """

    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticModelSerializer
    permission_classes = [IsVeterinary | IsManager]
