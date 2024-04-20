from rest_framework import serializers
from .models import Product

""" Convert Model object to serialized JSON object """

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id"]
