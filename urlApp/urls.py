from django.urls import path
from .views import DataUrlListCreateAPIView

urlpatterns = [
    path("", DataUrlListCreateAPIView.as_view())
]


