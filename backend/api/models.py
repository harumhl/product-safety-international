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
#     barcode = models.TextField()
#     createdAt = models.DateTimeField(auto_now_add=True)

# class Chemical(models.Model):
#     id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4().hex)
#     createdAt = models.DateTimeField(auto_now_add=True)

# class ProductChemical(models.Model):
#     pass
