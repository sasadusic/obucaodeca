from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UpdateProfileForm, CustomPasswordChangeForm
from django.contrib.auth import get_user_model
from .forms import ObucaForm, ObucaFormSet
from .models import Obuca, Odeca, SlikaObuce, SlikaOdece

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Wellcome {username.title()}, you are logged in')
            return redirect('index')
        else:
            messages.success(request, f'Wrong username or password please try again')
            return redirect('index')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    messages.success(request, f'You are logged out, Login to continue')
    logout(request)
    
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Wellcome {username.title()}, you are registered')
            return redirect('index')

    else:
        form = SignUpForm()

        return render(request, 'register.html', {'form': form})
        
    return render(request, 'register.html', {'form': form})

@login_required(login_url="login")
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url="login")
def  update_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = UpdateProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile has been updated successfully!")
            return redirect("profile")
        else:
            messages.error(request,"Please correct the error below.")
    else:
        form = UpdateProfileForm(instance=current_user)
    
    context={"form":form}
    return render(request,'update_profile.html',context)    

@login_required(login_url="login")
def change_password(request):
    current_user = request.user
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=current_user, data=request.POST)
        if form.is_valid():
            form.save()
            # Logout the user first to get rid of session cookie
            logout(request)
            messages.warning(request, "Password changed successfully! Please login again.")
            return redirect('logout')
        else:
            messages.error(request, "Error in password reset. Please try again.")
            
    else:
        form = CustomPasswordChangeForm(user=current_user)
        
    return render(request, 'change_password.html', {'form': form})

User = get_user_model()

@login_required(login_url="login")
def delete_profile(request):
    """
    View function for deleting a user's profile.
    Only accessible to authenticated users.
    """
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        user.delete()
        return redirect("index")
    
def kreiraj_obucu(request):
    if request.method == 'POST':
        form = ObucaForm(request.POST, request.FILES)
        formset = ObucaFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            obuca = form.save()
            formset.instance = obuca
            formset.save()
            return redirect('sva_obuca')
    else:
        form = ObucaForm()
        formset = ObucaFormSet()
    return render(request, 'kreiraj_obucu.html', {'form': form, 'formset': formset})

def sva_obuca(request):
    obuca = Obuca.objects.all()
    slike = SlikaObuce.objects.all()
    for o in obuca:   
        for slika in o.slike.all():
            print(slika.slika.url)
    return render(request, 'sva_obuca.html', {'obuca': obuca, 'slike': slike})

def detalji_obuce(request, pk):
    obuca = Obuca.objects.get(pk=pk)
    slike = SlikaObuce.objects.filter(obuca=obuca)
    return render(request, 'detalji_obuce.html', {'obuca': obuca, 'slike':  slike})

lorem = 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laudantium, dolorum? Quam sed earum nostrum, amet fuga vel quod pariatur accusamus.'