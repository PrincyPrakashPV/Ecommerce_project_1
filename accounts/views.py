from django.shortcuts import redirect, render
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        email=request.POST["email"]
        password1=request.POST["password"]
        password2=request.POST["password2"]
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
            user.save()
            print('created')
            return redirect('/')
        else:
            messages.info(request,'password not matched')
            return redirect('register')
            

    return render(request,'registeration.html')

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('logged in')
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

