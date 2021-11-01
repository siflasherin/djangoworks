from django import forms
class NumWordForm(forms.Form):
    number=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))