from django.contrib import messages
from django.shortcuts import render, redirect
from .form import UserResgisterForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request) :
    if request.method == 'POST' :
        form = UserResgisterForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, f'Your account has been created')
            return redirect('login')
    else:
        form = UserResgisterForm()
    context = {
        'form' : form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request) :
    return render(request, 'users/profile.html')

@login_required
def edit(request) :
    if request.method == 'POST' :
        uform = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if uform.is_valid() :
            uform.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
    context = {
        'form' : uform,
    }
    return render(request, 'users/edit.html', context)