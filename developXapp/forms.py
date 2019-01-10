from django import forms


class CashAmount(forms.Form):
    cashamount = forms.IntegerField(label="Username", widget=forms.NumberInput(attrs={"class": "form-control"}))
