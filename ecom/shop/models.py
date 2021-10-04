from django.db import models


# Create your models here.

class Products(models.Model):
      username = models.CharField(max_length=200)
      password = models.CharField(max_digits=5)






