from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        birthday = request.POST['birthday']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if cpassword == password:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Sorry email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=email,first_name=first_name,last_name=last_name,password=password,email=email)
                user.save()
                print("User Created Sucessfully")
                return redirect('login')

        else:
            messages.info(request, "Sorry Password does not match")
            return redirect('register')
        #return redirect('/')

    return render(request,'reg.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        print("email and pass taken")
        user=auth.authenticate(username=email,password=password)
        print("user authentication")

        if user != None :
            auth.login(request,user)
            print("sucess login")
            return redirect('/')

        else:
            messages.info(request, "invalid credential")
            print("invalid login")
            return redirect('login')

    return render(request,'log.html')

@csrf_exempt
def logout(request):
   auth.logout(request)
   return redirect('/')

