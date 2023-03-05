from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('quotation', views.get_quote, name='quote'),
]
