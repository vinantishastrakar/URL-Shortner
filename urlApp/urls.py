from django.urls import path
from .views import DataUrlListCreateAPIView, DataUrlRedirect

urlpatterns = [
    path("", DataUrlListCreateAPIView.as_view()),
    path("<str:shorturl>/", DataUrlRedirect.as_view())
]


