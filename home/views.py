from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
def index(request):
    context = {
        'variable':"this ia sent "
    }
    return render(request, 'index.html', context)

   # return HttpResponse('this is home page')
def home(request):
    return render(request,'home.html',)
def about(request):
    return render(request, 'about.html', )

    #return HttpResponse('this is about page ')
def service(request):
   return render(request, 'service.html', )


 #return HttpResponse('<h1> hh</h1> ')
def contact (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'badya guru message sent ho gya ')

    return render(request, 'contact.html', )

    #return HttpResponse('this is contact page ')

   # return HttpResponse('contact us ')