from django.contrib import admin

# Register your models here.

from .models import car_model
admin.site.register(car_model)
