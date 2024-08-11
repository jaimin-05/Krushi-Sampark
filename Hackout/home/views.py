from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import data_set,CropDetails
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
@never_cache
# Create your views here.
def login_view(request):

    if request.method == 'POST':
        email = request.POST.get('email1')
        passwd = request.POST.get('password1')

        userr = authenticate(request, username=email, password=passwd)

        if userr is not None:
            login(request, userr)
            messages.add_message(request, messages.INFO, "Hello world.")
            return redirect('farmer_index')  # Redirect to the appropriate view
        else:
            messages.error(request, 'Incorrect Email or Password')
            return HttpResponse('fail')  # Redirect back to the login page

    return render(request, 'login.html')
@never_cache
def index(request):
    return render(request, 'index.html')
@never_cache
def signup_view(request):
    if request.method == 'POST':
        # Handle the signup form submission here
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profession = request.POST.get('profession')
        ph_no = request.POST.get('ph_no')
        

        new_d = data_set(
            ph_no=ph_no,
            full_name=full_name,
            email = email,
            profession = profession,
                    
        )
        new_d.save()  # Save to database
        User.objects.create_user(username=email,email=email, password=password)
        print("registration succesfull")
        messages.success(request, "Registration successful!")
        return redirect('login_view')  # Redirect to login page after signup
                
        
        
        
    return render(request, 'signup.html')

@never_cache
@login_required
def farmer_index(request):
    crop_details = CropDetails.objects.all()  # Fetch all records from the CropDetails table
    return render(request, 'farmer.html', {'crop_details': crop_details})
    # return render(request,'farmer.html')

@never_cache
@login_required
def cold_storage_index(request):
    return render(request,'Cold_Storage.html')

@never_cache
@login_required
def company_index(request):
    return render(request,'Company.html')

@never_cache
@login_required
def mill_index(request):
    return render(request,'Small_Mill_Owners.html')

@never_cache
def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required
def a_index(request):
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name')
        quantity = request.POST.get('quantity')
        due_date = request.POST.get('due_date')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        # Save the data to the database
        new_crop = CropDetails(
            crop_name=crop_name,
            quantity=quantity,
            due_date=due_date,
            address=address,
            phone_number=phone_number
        )
        new_crop.save()

        print("done bro")
        return redirect('a1_index')

    return render(request, 'addition.html')

def a1_index(request):
    if request.method =='POST':
        return redirect('farmer_index')
    return render(request,'addition1.html')