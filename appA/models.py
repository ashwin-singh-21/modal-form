from django.db import models

# Create your models here.

class car_model(models.Model):
    brand = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    manufacture_year = models.IntegerField(max_length=100)

    def __str__(self):
        return self.owner

