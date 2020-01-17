from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    adress = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
