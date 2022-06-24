from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def faq_list(request):
    """ A view to return the FAQ page """

    return render(request, 'home/faq.html')




def contact_us(request):
    """ A view to return the contact us page """
    form_class = ContactForm

    return render(request, 'home/contact_us.html', {
        'form': form_class,
    })