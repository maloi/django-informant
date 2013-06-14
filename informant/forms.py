from django import forms


class SubscribleNewsForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    surname = forms.CharField(required=False)
    back_url = forms.CharField(required=False)
