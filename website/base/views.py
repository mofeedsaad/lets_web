from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

from .models import *
from .forms import CreateUserForm

# Create your views here.



def registerpage(request):

 if request.user.is_authenticated:
     return redirect('home')
 else:
    form = CreateUserForm()
    if request.method == 'POST':
       form = CreateUserForm(request.POST)
    if form.is_valid():
          form.save()
          user = form.cleaned_data.get('username')

          messages.success(request,'Account was created for ', + user)
          return redirect('login')

    context ={'form': form}
    return render(request, 'base/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
      if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if  user is not None:
            login(request,user)
            return redirect('home')
        else :
            messages.info(request,'Username OR password is incorrect')
            

    context = {}
    return render(request, 'base/login.html',context)

def search(request):
    q = request.GET['q']
    results = product.objects.filter(name__icontains=q).order_by('-id')
    return render(request, 'search.html', {'results': results})


@login_required(login_url='login')
def userPage(request):
    context = {}
    return render (request,'base/user.html',context)

def logoutUser(request):
    logout(request)
    return redirect ('login')

@login_required(login_url='login')
def home(request):
    
    products = product.objects.all()
    context = {'products':products}
    return render(request,'base/main.html',context)
@login_required(login_url='login')
def products(request):
    return render(request,'base/products.html')
@login_required(login_url='login')
def customer(request):
    return render(request,'base/customer.html')

def product_detail(request,slug,id):
    return render(request,'base/product_detail.html')