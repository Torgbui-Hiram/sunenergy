from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('quotation', views.get_quote, name='quote'),
    path('message', views.send_message, name='message'),
    path('about', views.about_page, name='about'),
    path('all', views.all_services, name='service'),
]
