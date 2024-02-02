from django.shortcuts import render,HttpResponse
from home.models import contact
from datetime import datetime


# Create your views here.
def home(request):
    return render(request,'index.html')

def not_programming(request):
    return render(request,'not_coding.html')

def what_im_doing(request):
    return render(request,'what_im_doing.html')

def faq(request):
    return render(request,'faq.html')

def Contact(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        Text = request.POST.get("Text")
        contactobj = contact(
            firstName=firstName,
            lastName=lastName,
            email=email,
            Text=Text,
            date=datetime.now(),
        )
        contactobj.save()
        return HttpResponse("Thanks for Submitting")
    return render(request,"contact.html")