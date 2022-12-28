from rest_framework.routers import DefaultRouter
from apps.clinic.api.api import AnalysisViewset

router = DefaultRouter()
router.register(r"analysis", AnalysisViewset, basename="analysis")
router.register(r"treatments", AnalysisViewset, basename="treatments")


urlpatterns = router.urls
