from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import DataUrl
from .serializers import DataUrlSerializer

# Create your views here.

class DataUrlListCreateAPIView(APIView):
    def get(self,request):
        urls = DataUrl.objects.all()
        serializer = DataUrlSerializer(urls, many=True, context={'request':request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DataUrlSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DataUrlRedirect(APIView):

    def get(self, request, shorturl):
        url = get_object_or_404(DataUrl, shorturl=shorturl)
        url.save()
        return redirect(url.longurl)