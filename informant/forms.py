from django import forms


class SubscribleNewsForm(forms.Form):
    email = forms.EmailField()
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    surname = forms.CharField(required=False)
    back_url = forms.CharField(required=False)
