from charset_normalizer import models
from django.shortcuts import render , redirect
from django.contrib import messages
from flask_login import login_required
from .forms import UserRegisterForm, UserUpdateForm, profileUpdateForm
from django.contrib.auth.decorators import login_required


def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success (request, f'Yay you have created an acount, please login!! !')
            return redirect ('login')
    else:
        form = UserRegisterForm()
    return render (request, 'users/register.html', {"form":form})

@login_required
def profile (request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user) 
        p_form = profileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success (request, f'Your account has been updated!! !')
            return redirect ('profile')
    else:
        u_form = UserUpdateForm(instance=request.user) 
        p_form = profileUpdateForm(instance=request.user.profile)
    contex = {
        'u_form': u_form,
        'p_form' : p_form
    }
    return render (request, 'users/profile.html',contex)


    