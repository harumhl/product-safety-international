from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer

class ProductListApiView(APIView):
    # # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(id = 'c4f60480-c6a3-4c88-9c41-34440afddd58')
        # todos = Todo.objects.filter(user = request.user.id)
        serializer = ProductSerializer(products, many=True)
        return HttpResponse(serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'id': 'c4f60480-c6a3-4c88-9c41-34440afddd58'
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)

        return HttpResponse(serializer.errors)
