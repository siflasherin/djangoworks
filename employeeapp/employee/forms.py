from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-class"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-class"}))