from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def faq_list(request):
    """ A view to return the FAQ page """

    return render(request, 'home/faq.html')