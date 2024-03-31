# bulk_sender/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_bulk_messages, name='send_bulk_messages'),
    path('whatsapp.html',views.send_whatsapp),
    path('SMS.html',views.send_sms,),
    path('Email.html',views.my_form_view),
]
