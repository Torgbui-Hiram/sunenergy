from django.forms import Form
from django.forms.models import ModelForm
from . models import Quotation


class QuotationForm(ModelForm):
    class Meta:
        model = Quotation
        fields = ('name', 'email', 'phone', 'requirement')
