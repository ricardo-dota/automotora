from django.db.models.expressions import OrderBy
from django.shortcuts import render,redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate( username = username , password = password)
            if user is not None:
                auth.login(request,user)
                messages.success(request, 'Estas logeado' )
                return  redirect('dashboard')
            else:
                messages.error(request, 'Datos incorrectos' )
                return  redirect('login')
        except:
            return  redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        #messages.error(request, 'Datos invalidos' )
        username         = request.POST['username']
        email            = request.POST['email']
        password         = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter( username = username).exists():
                messages.error( request , 'El Usuario ya existe')
                return  redirect('register')
            else:
                if User.objects.filter( email = email).exists():
                     messages.error( request , 'Email ya existe')
                     return  redirect('register')
                else:
                    user = User.objects.create_user( username = username , email = email , password = password)
                    try:
                        user.save()
                        auth.login(request,user)
                        messages.success( request , 'Exito ahora estas logeado')
                        return  redirect('dashboard')
                    except:
                        messages.error(request,'Ha existido un error al crear al usuario')
                        return  redirect('register')
        else:
            messages.error(request,'Los password deben ser iguales')  
            return  redirect('register')  
    else:    
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success( request , 'Session finalizada con exito')
        return redirect('login')
    else:
        return redirect('home')


@login_required( login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter( user_id = request.user.id)
    data = {
        'inquires' : user_inquiry
    }
    return render(request, 'accounts/dashboard.html',data)