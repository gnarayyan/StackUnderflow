from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from usercontrol.models import UserProfile
from django.contrib.auth import authenticate
# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('Form Submitted')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        print('Invalid Data')
    print('loading form')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('usermail')
        password1 = request.POST.get('password')
        password2 = request.POST.get('passwordconfirm')
        image = request.FILES.get('userimage')
        print('Form Submitted')
        if (password1 == password2):
            if not User.objects.filter(username=username).exists():
                print('Creating User')
                user = User.objects.create_user(username=username, password=password1,
                                                email=email)
                user.save()
                userProfile = UserProfile.objects.create(
                    user=user, avatar=image)
                userProfile.save()
                return redirect('login')
        print('Invalid Data')
    print('loading form')
    return render(request, 'signup.html')
