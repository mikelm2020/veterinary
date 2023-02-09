from apps.users.api.api import LoginView
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from knox import views as knox_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"login/", LoginView.as_view(), name="knox-login"),
    path(r"logout/", knox_views.LogoutView.as_view(), name="knox-logout"),
    path(r"logoutall/", knox_views.LogoutAllView.as_view(), name="knox-logoutall"),
    path("", include("apps.users.api.routers")),
    path("", include("apps.clinic.api.routers")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "doc/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
