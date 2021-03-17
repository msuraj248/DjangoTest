from django.shortcuts import render, HttpResponse
from datetime import datetime
from application.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        messages.success(request, "Your Request has been Processed")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('This is about page')

def services(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        contact = Contact(name=name, mail=mail, contact=contact, address=address, date = datetime.today())
        contact.save()
        
    return render(request,'services.html')
    # return HttpResponse('This is my services page')

def contact(request): 
    return render(request,'contact.html')
    # return HttpResponse('This is myP contact page')

