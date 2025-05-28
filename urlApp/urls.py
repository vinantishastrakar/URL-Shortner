from django.urls import path
from .views import DataUrlListCreateAPIView, DataUrlRedirect, DataUrlRetrieveUpdateDestroyAPIView, index

urlpatterns = [
    path("urls/", DataUrlListCreateAPIView.as_view()),
    path("urls/<str:shorturl>/", DataUrlRetrieveUpdateDestroyAPIView.as_view()),
    path("", index),
    path("<str:shorturl>/", DataUrlRedirect.as_view()),
]


