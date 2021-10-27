from django import forms
from django.forms import ModelForm
from mobile.models import Mobile


# class MobileAddForm(forms.Form):
#     mobile_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     model=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     colour=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     storage=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     copies=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         #validation check content only
#         price = cleaned_data["price"]
#         copies=cleaned_data["copies"]
#         storage=cleaned_data["storage"]
#
#         if price < 0:
#             msg="invalid price"
#             self.add_error("price",msg)
#         if copies < 0:
#             msg="invalid copies"
#             self.add_error("copies",msg)
#         if storage < 0:
#             msg="invalid storage"
#             self.add_error("storage",msg)

class MobileAddForm(ModelForm):
    class Meta:
        model = Mobile
        fields = ["mobile_name", "model", "colour", "storage", "copies", "price","image", ]
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "colour": forms.TextInput(attrs={"class": "form-control"}),
            "storage": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }
