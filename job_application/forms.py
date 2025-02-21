from django import forms

class JobApplicationForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    date = forms.DateField()
    occupation = forms.CharField(max_length=100)