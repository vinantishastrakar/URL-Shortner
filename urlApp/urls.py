from django.urls import path
from .views import DataUrlListCreateAPIView, DataUrlRedirect, DataUrlRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", DataUrlListCreateAPIView.as_view()),
    path("<str:shorturl>/", DataUrlRedirect.as_view()),
    path("urls/<str:shorturl>/", DataUrlRetrieveUpdateDestroyAPIView.as_view())
]


