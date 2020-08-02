from django import forms
from .models import car_model


class employee(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    salary = forms.IntegerField()
    status = forms.BooleanField()

class sample(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    contact = forms.IntegerField()
    status = forms.BooleanField()

class car_gallery(forms.ModelForm):
    class Meta:
        model = car_model
        fields = ('brand','owner','manufacture_year')