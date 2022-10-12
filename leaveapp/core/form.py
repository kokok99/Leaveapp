
from random import choices
from tkinter import Widget
from django import forms
from .models import Application, Staff

class DateInput(forms.DateInput):
    input_type = 'date'

class Pemohon(forms.ModelForm) :
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'type' : 'text',
        'list' : 'staff'
    }))
    class Meta:
        model = Staff
        fields = ['fullname']

class ApplyLeaveForm(forms.ModelForm):
    LEAVE_CHOICES = (
        ('Pilih Cuti', 'Pilih Cuti'),
        ('Cuti Tahunan', 'Cuti Tahunan'),
        ('Cuti Sakit', 'Cuti Sakit'),
        ('Cuti Kecemasan', 'Cuti kecemasan'),
        ('Cuti Bersalin', 'Cuti Bersalin'),
        ('Cuti Haji', 'Cuti Haji'),
        ('Cuti Umrah', 'Cuti Umrah'),
    )
    pemohon = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'exampleDataList',
        'list' : 'staff'
    }))
    days = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class' : 'form-control',
    }))
    leave = forms.ChoiceField(choices=LEAVE_CHOICES ,widget=forms.Select(attrs={
        'class' : 'form-control',
    }))
    details = forms.CharField(widget= forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder': 'Details',
                'rows' : 3,
                }))
    class Meta:
        model = Application
        fields = ['pemohon','leave', 'details', 'attachment', 'from_date', 'to_date', 'days']
        widgets = {
            'from_date': DateInput(attrs={
                'class': 'form-control'
            }),
            'to_date' : DateInput(attrs={
                'class' : 'form-control'
            }),
        }


class Approval(forms.ModelForm):
    STATUS_CHOICES = (
        ('Approve', 'Approve'),
        ('Reject', 'Reject')
    )
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect(attrs={
        'font-size' : '20px'
    }))
    class Meta:
        model = Application
        fields = ['status']

class AddStaff(forms.ModelForm):
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
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
    }))
    cawangan = forms.ChoiceField(choices=CAWANGAN_CHOICES ,widget=forms.Select(attrs={
        'class' : 'form-control',
    }))
    class Meta:
        model = Staff
        fields = ['fullname', 'email', 'phone', 'address', 'image', 'cawangan']

class EditLeave(forms.ModelForm) :
    class Meta:
        
        model = Staff
        fields = ['tahunan', 'sakit', 'bersalin', 'umrah', 'haji']
        widgets = {
            'tahunan': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'sakit': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'bersalin': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'umrah': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'haji': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }
        