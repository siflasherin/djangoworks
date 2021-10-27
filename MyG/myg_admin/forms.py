from django import forms
from django.forms import ModelForm
from myg_admin.models import Appliences

class ApplienceAddForm(ModelForm):
    class Meta:
        model=Appliences
        fields="__all__"
        widgets={
            "applience_name":forms.TextInput(attrs={"class":"form-control"}),
            "copies":forms.NumberInput(attrs={"class":"form-control"}),

        }