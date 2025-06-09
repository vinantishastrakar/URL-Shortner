from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import DataUrl
from .serializers import DataUrlSerializer


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
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


@method_decorator(csrf_exempt, name='dispatch')
class DataUrlRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, shorturl):
        url = get_object_or_404(DataUrl, shorturl=shorturl)
        serializer = DataUrlSerializer(url, context={"request":request})
        return Response(serializer.data)
    
    def put(self, request, shorturl):
        url = get_object_or_404(DataUrl, shorturl=shorturl)
        serializer = DataUrlSerializer(url, data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, shorturl):
        url = get_object_or_404(DataUrl, shorturl=shorturl)
        url.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@method_decorator(csrf_exempt, name='dispatch')       
class DataUrlRedirect(APIView):
    def get(self, request, shorturl):
        url = get_object_or_404(DataUrl, shorturl=shorturl)
        url.save()
        return redirect(url.longurl)
    
def index(request):
    return render(request = request, template_name = "urlApp/index.html", context = {})