from ast import Num
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect

from booking_PFA.settings import BASE_DIR
import json
import os
from  django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger

from .models import Contact
# Create your views here.

# def home(request):
#     if 'user' in request.session:
#         current_user = request.session['user']
#         param = {'current_user': current_user}
#         return render(request, 'base.html', param)
#     else:
#         return redirect('login')
#     return render(request, 'login.html')


def home(request):
    # load JSON
    json_data = os.path.join(BASE_DIR, 'static', "JSON/Hotel.json")
    with open(json_data) as f:
        Hotels = json.load(f)
    title="Home"


    p =Paginator(Hotels['Hotels'],12)

    #number of pages

    Num_page = request.GET.get('page',1)

    try:
        page = p.page(Num_page)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page= p.page(1)

    

    return render(request,'home/home.html',{'title':title,'Hotels':page})




def template(request):
    title="template"
    return render(request,'home/template.html',{'title':title})

def contact(request):
    if(request.POST):
        try:
            title="Contact Posted"

            ### Create object
            c=Contact(name=request.POST['name'],email=request.POST['email'],message=request.POST['message'])
            c.save()
            message=['Your mesage has been submitted  successfully!','success']

            return render(request,"home/contact.html",{'title':title,'message':message})
        except Exception as e:
            message=[e,'Erreur']
            return render(request,"home/contact.html",{'title':title,'message':message})
    else:
        title="Contact"
        return render(request,"home/contact.html",{'title':title})


def error_404_view(request, exception):
    title="404"
    return render(request, 'errors/404.html',{'title':title},status=404)

def error_500_view(request):
    title="500"
    return render(request, 'errors/500.html',{'title':title},status=500)
