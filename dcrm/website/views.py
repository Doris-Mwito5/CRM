from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in successfully")
            return redirect('home')
        else:
            messages.success(request, "An error occured")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New account created successfully!")
            return redirect('home')
            #Authenticate and login
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(username=username, password=password)
            # login(request,user)
            # messages.success(request, "You have successfully signed in")
            # return redirect('home')
    else:
        register_form = SignUpForm()    
        return render(request, 'register.html', {'register_form': register_form})
    return render(request, 'register.html', {'register_form': register_form}) 