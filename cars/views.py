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
    model_search = Cars.objects.values_list( 'model' , flat=True).distinct()
    state_search = Cars.objects.values_list( 'state' , flat=True).distinct()
    year_search = Cars.objects.values_list( 'year' , flat=True).distinct()
    body_Style_search = Cars.objects.values_list( 'body_Style' , flat=True).distinct()

    context = {
        'cars':paged_cars,
        'model_search' : model_search,
        'state_search':state_search,
        'year_search':year_search,
        'body_Style_search': body_Style_search,
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

    model_search = Cars.objects.values_list( 'model' , flat=True).distinct()
    state_search = Cars.objects.values_list( 'state' , flat=True).distinct()
    year_search = Cars.objects.values_list( 'year' , flat=True).distinct()
    body_Style_search = Cars.objects.values_list( 'body_Style' , flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            cars = cars.filter( Q(description__icontains = keyword) |  Q( car_title__icontains = keyword) ) 

    if 'model' in request.GET:
        model = request.GET.get('model')
        if model:
            cars = cars.filter( Q(model__iexact = model) ) 

    if 'state' in request.GET:
        state = request.GET.get('state')
        if state:
            cars = cars.filter( Q(model__iexact = state) ) 

    if 'body' in request.GET:
        body = request.GET.get('body')
        if body:
            cars = cars.filter( Q(body_Style__iexact = body))
    
    if 'year' in request.GET:
        year = request.GET.get('year')
        if year:
            cars = cars.filter( Q(year__iexact = year) )


    if 'min_price' in request.GET:
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if max_price:
            cars = cars.filter( price__gte = min_price , price__lte = max_price )



    data = {
        'cars':cars,
        'model_search' : model_search,
        'state_search':state_search,
        'year_search':year_search,
        'body_Style_search': body_Style_search,
    }
    return render(request , 'cars/search.html',data) 