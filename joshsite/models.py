from django.db import models

# Create your models here.
class MyModel(models.Model):
    fullname = models.CharField(max_length=500)
    mobile_number = models.IntegerField()