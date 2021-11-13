from django import forms
from django.forms import ModelForm
from book.models import Book, Orders


# class BookAddForm(forms.Form):
#     book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     no_of_copies=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean() #child class parent classine override cheyunnu.ennit cleaned data dictionary aayi store cheyyunnu
#         # cleaned data after default cleaning of parent class
#         price=cleaned_data["price"]
#         copies=cleaned_data["no_of_copies"]
#
#         if price < 0:
#             # print("invalid price")
#             msg = "invalid price"
#             self.add_error("price",msg)
#
#         if copies < 0 :
#             msg="invalid no of copies"
#             self.add_error("no_of_copies",msg)

class BookAddForm(ModelForm):
    class Meta:
        model = Book
        fields = ["book_name", "author", "price", "copies", "image", ]
        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"})
        }
        # labels={
        #     "book_name":"BOOK_NAME"
        # }


class OrderUpdateForm(ModelForm):
    class Meta:
        model = Orders
        fields = ["status", "expected_delivery_date"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-select"}),
            "expected_delivery_date": forms.DateInput(attrs={"type":"date","class": "form-select"}),
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
