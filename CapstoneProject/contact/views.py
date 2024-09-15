from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            response_message = 'HUMAN!'
        else:
            response_message = 'BOT!'
        
        return render(request, 'contact/response.html', {
            'response_message': response_message,
            'next_url': request.META.get('HTTP_REFERER')  # Get the previous URL
        })
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
