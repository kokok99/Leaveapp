from email.policy import default
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Role

class UserResgisterForm(UserCreationForm) :
    CAWANGAN_CHOICES = (
        ('Choose cawangan', 'Choose cawangan'),
        ('PASTI SEMBULAN', 'PASTI SEMBULAN'),
        ('PASTI ASY SYAKIRIN', 'PASTI ASY SYAKIRIN'),
        ('PASTI RAUDAH', 'PASTI RAUDAH'),
        ('PASTI PETAGAS', 'PASTI PETAGAS'),
        ('PASTI CERIAMAS', 'PASTI CERIAMAS'),
        ('PASTI PASIR PUTIH', 'PASTI PASIR PUTIH'),
        ('PASTI KETIAU', 'PASTI KETIAU'),
    )
    email = forms.EmailField(widget= forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
                }))
    password1 =  forms.CharField(widget= forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                }))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Retype password'
                }))
    is_admin = forms.BooleanField(required=False)
    
    
    cawangan = forms.ChoiceField(choices=CAWANGAN_CHOICES ,widget=forms.Select(attrs={
        'class' : 'custom-select'
    }))
    class Meta:
        model = Role
        fields = ['username', 'email', 'password1', 'password2', 'is_admin', 'is_superuser', 'cawangan']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),       
        }

class UserUpdateForm(forms.ModelForm):
    CAWANGAN_CHOICES = (
        ('Choose cawangan', 'Choose cawangan'),
        ('PASTI SEMBULAN', 'PASTI SEMBULAN'),
        ('PASTI ASY SYAKIRIN', 'PASTI ASY SYAKIRIN'),
        ('PASTI RAUDAH', 'PASTI RAUDAH'),
        ('PASTI PETAGAS', 'PASTI PETAGAS'),
        ('PASTI CERIAMAS', 'PASTI CERIAMAS'),
        ('PASTI PASIR PUTIH', 'PASTI PASIR PUTIH'),
        ('PASTI KETIAU', 'PASTI KETIAU'),
    )
    email = forms.EmailField(widget= forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
                }))
    phone = forms.CharField(widget= forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Phone Number'
                }))
    address = forms.CharField(widget= forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Address'
                }))
    cawangan = forms.ChoiceField(choices=CAWANGAN_CHOICES ,widget=forms.Select(attrs={
        'class' : 'custom-select'
    }))

    class Meta:
        model = Role
        fields = ['username', 'email', 'phone', 'address', 'cawangan', 'image']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Name'
                }),       
        }

    