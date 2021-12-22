from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserRegisterForm(data = request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now log in.')
            return redirect('Users:login')
            

    form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form })

def logout_view(request):
    logout(request)
    messages.success(request, 'You logged out.')
    return redirect('Users:login')

@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdate(instance = request.user, data = request.POST)
        profile_form = ProfileUpdate(request.POST,request.FILES, 
                                     instance = request.user.profile,
                                    )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Profile updated.')
            return redirect('/')
    else:
        user_form = UserUpdate(instance = request.user)
        profile_form = ProfileUpdate(instance = request.user.profile)
        context = {'user_form':user_form, 'profile_form': profile_form}
        return render(request, 'users/profile.html', context)

    
    