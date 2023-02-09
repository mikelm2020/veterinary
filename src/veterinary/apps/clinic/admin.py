from django.contrib import admin
from apps.clinic.models import Analysis, Treatment, Hospitalization

admin.site.register(Analysis)
admin.site.register(Treatment)
admin.site.register(Hospitalization)


