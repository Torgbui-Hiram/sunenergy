from django.shortcuts import render, redirect
from .forms import QuotationForm, TrialForm
from django.contrib import messages
from django.core.mail import send_mail
from twilio.rest import Client
from decouple import config
# Create your views here.


client = Client(config('TWILIO_ACCOUNT_SID'), config('TWILIO_AUTH_TOKEN'))


def index(request):
    return render(request, 'index.html')


def get_quote(request):
    form = QuotationForm()
    subj = 'SOLAR AND INVERTER INSTALLATION QUOTE'
    mes = 'Hi! custormer, thank you for your interest in solar energy'
    if request.method == "POST":
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            name = request.POST['name']
            # phone = request.POST['phone']
            # Message using twilio
            # client.messages.create(to=phone, from_=config('TWILIO_PHONE_NUMBER'), body='Thank you for requesting a quote from Sunenergy'
            #                        )
            # Email using google smtp
            send_mail(subject=subj, message=mes, from_email=config(
                'EMAIL_HOST_USER'), recipient_list=[email,], fail_silently=True)
            messages.success(
                request, 'Your quotation has been submitted successfully')
            return redirect('home')
        else:
            messages.success(
                request, 'There was a problem with your form. try again')
    return render(request, 'quote.html', {'form': form})


def send_message(request):
    form = TrialForm(request.POST)
    if form.is_valid():
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        print(email, name, phone)
    return render(request, 'message.html', {})
