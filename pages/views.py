from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Team 
from cars.models import Cars
from django.core.mail import send_mail
from .forms import ContactForm


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    teams = Team.objects.all().order_by('-created_date')
    features_cars  = Cars.objects.all().order_by('-created_date').filter(is_featured = True)  
    latest_cars    = Cars.objects.order_by('-created_date') 
    #search_fields  = Cars.objects.values( 'model' , 'state' , 'year' , 'body_Style' )
    model_search = Cars.objects.values_list( 'model' , flat=True).distinct()
    state_search = Cars.objects.values_list( 'state' , flat=True).distinct()
    year_search = Cars.objects.values_list( 'year' , flat=True).distinct()
    body_Style_search = Cars.objects.values_list( 'body_Style' , flat=True).distinct()

    data = {
        'teams':teams,
        'features_cars' : features_cars,
        'latest_cars': latest_cars,
        #'search_fields':search_fields,
        'model_search' : model_search,
        'state_search':state_search,
        'year_search':year_search,
        'body_Style_search': body_Style_search,
    }

    return  render(request, 'pages/home.html',data)

def about(request):

    teams = Team.objects.all().order_by('-created_date')
    data = {
        'teams':teams
    }

    return  render(request, 'pages/about.html',data)

def services(request):
    return  render(request, 'pages/services.html')

def cars(request):
    return  render(request, 'pages/cars.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name    = form.cleaned_data['name']
            email   = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            phone   = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'devantoniomorales@gmail.com', ['devantoniomorales@gmail.com'])
                messages.success(request,'Gracias pro contactarse con nosotros')
            except BadHeaderError:
                messages.error(request,'Lo sentimos ha exitido un error al enviar ele mail')
            return redirect('contact')
        else:
            messages.error(request,'Los datos del ingresados no son correctos')
            return redirect('contact')
    else:
        form = ContactForm()
        context = {
            'form' : form
        }
        return  render(request, 'pages/contact.html',context)




