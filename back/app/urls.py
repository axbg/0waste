from django.urls import path
from .views import AppRoot, FastTrackEndpoint, ImpactMeasurementEndpoint, CatalogueEndpoint

urlpatterns = [
    path('hello', AppRoot.as_view()),
    path('fast', FastTrackEndpoint.as_view()),
    path('impact', ImpactMeasurementEndpoint.as_view()),
    path('catalogue', CatalogueEndpoint.as_view())
]