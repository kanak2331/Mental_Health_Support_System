from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'auth/contact.html', {'form': form})
