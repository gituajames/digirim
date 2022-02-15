from django import forms


class GetMapForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
