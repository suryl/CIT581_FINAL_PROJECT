from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user_name}'s review"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username