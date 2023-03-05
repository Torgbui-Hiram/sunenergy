from django.shortcuts import render, redirect
from .forms import QuotationForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def get_quote(request):
    form = QuotationForm()
    if request.method == "POST":
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your quotation has been submitted successfully')
            return redirect('home')
        else:
            messages.success(
                request, 'There was a problem with your form. try again')
    return render(request, 'quote.html', {'form': form})
