from apps.clinic.api import api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"analysis", api.AnalysisViewset, basename="analysis")
router.register(r"treatments", api.TreatmentViewset, basename="treatments")
router.register(
    r"hospitalizations", api.HospitalizationViewset, basename="hospitalizations"
)
router.register(r"proprietors", api.ProprietorViewset, basename="proprietors")
router.register(r"diseases", api.DiseaseViewset, basename="diseases")
router.register(r"pets", api.PetViewset, basename="pets")
router.register(r"receptions", api.ReceptionViewSet, basename="receptions")
router.register(r"displacements", api.DisplacementViewSet, basename="displacements")



urlpatterns = router.urls
