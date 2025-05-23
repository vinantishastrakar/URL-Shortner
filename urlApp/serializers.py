from rest_framework import serializers
from .models import DataUrl

class DataUrlSerializer(serializers.ModelSerializer):
    short_code = serializers.SerializerMethodField()
    
    class Meta:
        model = DataUrl
        fields = ["__all__", "short_code"]
        read_only_fields = ["shorturl", "short_code"]

    def get_short_code(self,obj):
        request = self.context.get("request")
        if request:
            return f"{request.scheme}://{request.get_host()}/{obj.shorturl}"
        return obj.shorturl