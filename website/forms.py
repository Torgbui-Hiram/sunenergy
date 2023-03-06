from django.forms import Form
from django.forms.models import ModelForm
from . models import Quotation
from django import forms


class QuotationForm(ModelForm):
    class Meta:
        model = Quotation
        fields = ('name', 'email', 'requirement')
        


class TrialForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailInput()
    phone = forms.CharField(max_length=20)
