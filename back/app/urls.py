from django.urls import path
from .views import FastTrackEndpoint, ImpactMeasurementEndpoint, CatalogueEndpoint

urlpatterns = [
    path('fast', FastTrackEndpoint.as_view()),
    path('impact', ImpactMeasurementEndpoint.as_view()),
    path('catalogue', CatalogueEndpoint.as_view())
]