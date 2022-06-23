from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faq/', views.faq_list, name='faq'),
    path('contact_us/', views.contact_us, name='contact_us'),
]