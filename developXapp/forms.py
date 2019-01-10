from django import forms


class CashAmount(forms.Form):
    cashamount = forms.FloatField(label="Username", required=False, widget=forms.NumberInput(attrs={"class": "form-control"}))

# Im leaving the Float Field in this form on purpose, otherwise Django would validate NumberInput and would not allow to submit form
# so I would not be able to throw exception in Django
# also Im assuming that we are talking about some ATM keyboard so the user can not input other characters like letters etc.

