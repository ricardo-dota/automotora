from django.shortcuts import render
from .models import Cars
from django.shortcuts import get_object_or_404, redirect, render 
from django.core.paginator import PageNotAnInteger , EmptyPage , Paginator
from django.db.models import Q
#from django.contrib import 

# Create your views here.
def cars(request):
    cars = Cars.objects.order_by('-created_date')

    #paginador 

    paginator   = Paginator(  cars, 4 )
    page        = request.GET.get('page')
    paged_cars  = paginator.get_page(page)


    context = {
        'cars':paged_cars
    }
    return render(request , 'cars/cars.html',context)

def cars_detail(request, id ):

    car = get_object_or_404( Cars , id = id)

    context = {
        'car' : car
    }


    return render(request , 'cars/cars_detail.html' , context)

def search(request):

    cars = Cars.objects.order_by('-created_date')

    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            cars = cars.filter( Q(description__icontains = keyword) |  Q( car_title__icontains = keyword) ) 


    data = {
        'cars':cars
    }
    return render(request , 'cars/search.html',data) 