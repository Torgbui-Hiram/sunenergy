from django.contrib import admin
from .models import Quotation

# Register your models here.


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'requirement', 'quote_date')
    list_filter = ('name', 'email', 'phone', 'requirement', 'quote_date',)
