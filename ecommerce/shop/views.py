from django.shortcuts import render,redirect
from shop.models import Product
from django.http import HttpResponse
from shop.form import ProductForm
from .models import Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib import messages

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def pro(request):
    L=Product.objects.all()
    return render(request,'products.html',{'prdt':L})
    
def add(request):
    if request.method=='POST':
        pf=ProductForm(request.POST,request.FILES)
        if pf.is_valid():
            pf.save()
            return redirect('pro')
           
        else:
            return HttpResponse("invalid form")
    f=ProductForm()
    return render(request,'add_product.html',{'form':f})

def delete_product(request,pro_id):
    p=Product.objects.get(id=pro_id)
    p.delete()
    return redirect('pro')

def edit(request,pro_id):
    p=Product.objects.get(id=pro_id)
    f=ProductForm(request.POST or None,request.FILES or None, instance=p)
    if f.is_valid():
            f.save()
            return redirect('pro')
    return render(request,'add_product.html',{'form':f})

def search(request):
    n = request.POST['pname']
    p = Product.objects.filter(name__iexact=n)  
    return render(request, 'products.html', {'prdt': p})


def signup(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        fname = request.POST['Firstname']
        lname = request.POST['Lastname']
        em = request.POST['email']

       
        if pwd1 != pwd2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

      
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

       
        myuser = User.objects.create_user(username=uname, password=pwd1, email=em)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Account created successfully!")
        return redirect('signin')

    return render(request, "signup.html")


def signin(request):
    if request.method=='POST':
        uname = request.POST['username']
        pwd1 = request.POST['password1']
        red=authenticate(username=uname,password=pwd1)
        if red is not None:
            login(request,red)
            f=red.first_name
            l=red.last_name
            return render(request,'user_dashboard.html',{'fname':f,'lname':l})
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'signin.html')

def user_logout(request):
    logout(request)
    return redirect('home') 


