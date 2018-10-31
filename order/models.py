from django.db import models

# Create your models here.


class Waffle(models.Model):
    flavor = models.CharField(max_length=200)
    base = models.CharField(max_length=200)
    dressing = models.CharField(max_length=200)
    topping = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
