from django.contrib.auth import user_logged_in
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import UserProfile, BloodBagInfo, BloodBankInfo


# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    elif request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST ['fname']
        lname = request.POST ['lname']
        email = request.POST['email']
        phone = request.POST ['phone']
        age = request.POST ['age']
        address = request.POST ['address']
        zone = request.POST ['zone']
        blood = request.POST ['blood']
        gender =request.POST['gender']

        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            messages.info(request,'Email already in use') ###
            return render(request,'register.html')
        else:
            user = User.objects.create_user(first_name = fname, last_name = lname, email=email,password=password,username=email, is_staff = True)
            profile = UserProfile.objects.create(user=user, phone_number=phone, age=age, address=address, gender=gender, zone = zone, blood=blood)

            #login
            user = auth.authenticate(username=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')

    elif request.user.is_authenticated:
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    if user_logged_in:
        profile = UserProfile.objects.filter(user_id = request.user.id)
        return render(request, 'user_profile.html', {'profile_info': profile})
def dashboard(request):
    if user_logged_in:
        return render(request,'dashboard.html')

def about(request):
    return render(request, 'about.html')

def update_bank(zone, blood_type, quantity):
    blood_bank = BloodBankInfo.objects.get(branch_zone=zone)
    if blood_type == 'A+':
        blood_bank.a_positive += quantity
    elif blood_type == 'A-':
        blood_bank.a_negative += quantity
    elif blood_type == 'B+':
        blood_bank.b_positive += quantity
    elif blood_type == 'B-':
        blood_bank.b_negative += quantity
    elif blood_type == 'O+':
        blood_bank.o_positive += quantity
    elif blood_type == 'O-':
        blood_bank.o_negative += quantity
    elif blood_type == 'AB+':
        blood_bank.ab_positive += quantity
    elif blood_type == 'AB-':
        blood_bank.ab_negative += quantity

    blood_bank.save()


def entry(request):
    if request.method == 'POST':
        zone = request.POST.get('zone', '')
        date = request.POST.get('date', '')
        blood_type = request.POST.get('blood_type', '')
        quantity_str = request.POST.get('quantity', '')
        
        # Validate inputs
        if not zone or not date or not blood_type or not quantity_str:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'blood_entry.html')
        
        try:
            quantity = int(quantity_str)
        except ValueError:
            messages.error(request, 'Quantity must be a valid number')
            return render(request, 'blood_entry.html')
        
        if quantity <= 0:
            messages.error(request, 'Quantity must be greater than 0')
            return render(request, 'blood_entry.html')
        
        # Update bank info
        update_bank(zone, blood_type, quantity)
        
        # Create blood bag entry
        BloodBagInfo.objects.create(
            blood_group=blood_type,
            date=date,
            quantity=quantity,
            branch=zone
        )
        
        messages.success(request, f'Successfully added {quantity} units of {blood_type} blood to {zone} zone')
        return redirect('details')
    
    return render(request, 'blood_entry.html')

def details(request):
    blood = BloodBankInfo.objects.all()
    return render(request, 'blood_details.html', {'blood_info': blood})

def list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_list.html', {'users': users})

def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        username = user.username
        user.delete()
        messages.success(request, f'User {username} has been removed successfully')
    except User.DoesNotExist:
        messages.error(request, 'User not found')
    return redirect('list')

def donate(request):
    if request.method == 'POST':
        zone = request.POST.get('zone', '')
        date = request.POST.get('date', '')
        blood_type = request.POST.get('blood_type', '')
        quantity_str = request.POST.get('quantity', '')
        
        # Validate inputs
        if not zone or not date or not blood_type or not quantity_str:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'donate.html')
        
        try:
            quantity = int(quantity_str)
        except ValueError:
            messages.error(request, 'Quantity must be a valid number')
            return render(request, 'donate.html')
        
        if quantity <= 0:
            messages.error(request, 'Quantity must be greater than 0')
            return render(request, 'donate.html')
        
        quantity_negative = quantity * -1
        
        # Update bank info (deduct from inventory)
        update_bank(zone, blood_type, quantity_negative)
        
        # Create blood bag entry with negative quantity
        BloodBagInfo.objects.create(
            blood_group=blood_type,
            date=date,
            quantity=quantity_negative,
            branch=zone
        )
        
        messages.success(request, f'Successfully recorded donation of {quantity} units of {blood_type} blood from {zone} zone')
        return redirect('details')
    
    return render(request, 'donate.html')

def search(request):
    if request.method == 'POST':
        zone = request.POST.get('zone', '')
        blood_group = request.POST.get('blood_group', '')
        quantity_str = request.POST.get('quantity', '')
        
        # Validate that all fields are provided
        if not zone or not blood_group or not quantity_str:
            messages.error(request, 'Please fill in all fields')
            return render(request, 'search.html')
        
        try:
            quantity = int(quantity_str)
        except ValueError:
            messages.error(request, 'Quantity must be a valid number')
            return render(request, 'search.html')
        
        if quantity < 0:
            messages.error(request, 'Quantity cannot be negative')
            return render(request, 'search.html')
        
        avail = BloodBankInfo.objects.filter(branch_zone=zone)
        
        count = 0
        blood = ''
        
        for i in avail:
            if blood_group == 'a_positive':
                count = i.a_positive
                blood = 'A+'
            elif blood_group == 'a_negative':
                count = i.a_negative
                blood = 'A-'
            elif blood_group == 'b_positive':
                count = i.b_positive
                blood = 'B+'
            elif blood_group == 'b_negative':
                count = i.b_negative
                blood = 'B-'
            elif blood_group == 'o_positive':
                count = i.o_positive
                blood = 'O+'
            elif blood_group == 'o_negative':
                count = i.o_negative
                blood = 'O-'
            elif blood_group == 'ab_positive':
                count = i.ab_positive
                blood = 'AB+'
            elif blood_group == 'ab_negative':
                count = i.ab_negative
                blood = 'AB-'
        
        available = quantity <= count if count > 0 else False
        
        donors = UserProfile.objects.filter(zone=zone, blood=blood, is_donor=True)
        
        return render(request, 'search.html', {'availability': available, 'donors': donors})
    
    return render(request, 'search.html')


def update_active_status(request, user_id):
    user = UserProfile.objects.get(user_id=user_id)
    user.is_donor = not user.is_donor  # Toggle the status
    user.save()
    return redirect('profile')

