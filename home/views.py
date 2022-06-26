from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def faq_list(request):
    """ A view to return the FAQ page """

    return render(request, 'home/faq.html')


def contact_us(request):
    """ A view to return the contact us page """
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for contacting us!')
            return render(request, 'home/index.html')
        
    else:
        form = ContactForm()

        template = 'home/contact_us.html'

        context = {
            'form': form,
            
        }

        return render(request, template, context)
   