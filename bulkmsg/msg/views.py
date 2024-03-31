# bulk_sender/views.py
from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
import csv
from .sender import send_email,send_sms1,send_whatsapp_message

#from .sender import send_message
def send_bulk_messages(request):
    return render(request,'index.html')
def handle_uploaded_file(file):
    csv_data = []
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)
    for row in reader:
        csv_data.append(row)
    return csv_data

def send_whatsapp(request):
   if request.method == 'POST':
        message = request.POST.get('message')
        file = request.FILES.get('file_upload')
        print(file,message)
        if file:
            csv_data = handle_uploaded_file(file)
            # Process the data here if needed
            flattened_list = [item for sublist in csv_data for item in sublist]

            print(flattened_list)
            send_whatsapp_message(flattened_list,message)

            return render(request,'whatsapp.html')   
        else:
            return HttpResponseBadRequest('No file uploaded.')
   else:
        return render(request,'whatsapp.html')
   

def send_sms(request):
   if request.method == 'POST':
        message = request.POST.get('message')
        file = request.FILES.get('file_upload')
        print(file,message)
        if file:
            csv_data = handle_uploaded_file(file)
            # Process the data here if needed
            flattened_list = [item for sublist in csv_data for item in sublist]

            print(flattened_list)
            send_sms1(flattened_list,message)

            return render(request,'SMS.html')   
        else:
            return HttpResponseBadRequest('No file uploaded.')
   else:
        return render(request,'SMS.html')


def my_form_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        file = request.FILES.get('file_upload')
        print(file,message)
        if file:
            csv_data = handle_uploaded_file(file)
            # Process the data here if needed
            flattened_list = [item for sublist in csv_data for item in sublist]

            print(flattened_list)
            send_email1(flattened_list,message)

            return render(request,'Email.html')   
        else:
            return HttpResponseBadRequest('No file uploaded.')
    else:
        return render(request,'Email.html')

