from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, RecordForm
from .models import Customer


def home(request):
    customers = Customer.objects.all()
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
        return render(request, 'home.html', {'customers':customers})
    
    
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

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up customers
        customer_record = Customer.objects.get(id=pk)
        return render(request, 'customer.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be Logged in")
        return redirect('home')        
 
def delete_record(request,pk):
     if request.user.is_authenticated:
         delete_it = Customer.objects.get(id=pk)
         delete_it.delete()
         messages.success(request, "Record deleted successfully")
         return redirect('home')
     else:
         messages.success(request, "You must be Logged in")
         return redirect('home')
             
def add_record(request):
    form = RecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "A New Record added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.error(request, "You must be Logged in")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Customer.objects.get(id=pk)
        form = RecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been Updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:        
        messages.error(request, "You must be Logged in")
        return redirect('home')