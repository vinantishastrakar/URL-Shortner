from rest_framework import serializers
from .models import DataUrl

class DataUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataUrl
        fields = "__all__"
        