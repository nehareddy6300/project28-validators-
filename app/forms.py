from typing import Any
from django import forms
from django.core import validators

def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('startswith a')


class SchoolForm(forms.Form):
    sname=forms.CharField(validators=[validate_for_a,validators.MinLengthValidator(3)])
    slocation=forms.CharField()
    sprincipal=forms.CharField()
    email=forms.EmailField()
    renteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('bot')
     
def clean(self):
    e=self.cleaned_data['email']
    re=self.cleaned_data['renteremail']
    if e!=re:
        raise forms.ValidationError('email not matchrd')
