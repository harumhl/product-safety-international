from django.db import models
# from django.contrib.auth.models import User
import uuid

"""
Run below commands after making changes
- `python manage.py makemigrations api`
- `python manage.py migrate api`
"""

class Product(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4().hex)
    barcode = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class Chemical(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4().hex)
    createdAt = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

class ProductTranslation(models.Model):
    language = models.TextField(null=False) # from https://en.wikipedia.org/wiki/IETF_language_tag
    name = models.TextField(null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class ChemicalTranslation(models.Model):
    language = models.TextField(null=False) # from https://en.wikipedia.org/wiki/IETF_language_tag
    name = models.TextField(null=False)
    score = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)

class ChemicalDetails(models.Model):
    details = models.TextField()
    source = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    chemicalTranslation = models.ForeignKey(ChemicalTranslation, on_delete=models.CASCADE)

