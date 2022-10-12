import csv
import io
from django.shortcuts import render, redirect, HttpResponse
from .models import Application, Staff
from users.models import Role
from django.contrib.auth.decorators import login_required, permission_required
from .form import ApplyLeaveForm, Approval, AddStaff, EditLeave, Pemohon
from django.contrib import messages
from .models import Application
from users.models import Role
from datetime import date
from django.core.mail import send_mail
from django.db.models import Q
from django.template.loader import get_template
from xhtml2pdf import pisa
from .filters import AppFilter



@login_required
def home(request) :
    user = Staff.objects.all()
    context = {
        'user' : user,
    }
    return render(request, 'core/home.html', context)

#Dashboard for admin and staff -----------------------------------------------------------------------------
@login_required
def index(request) :
    app = Application.objects.all()
    staff = Staff.objects.all()
    count = Staff.objects.all().count()
    approve = Application.objects.filter(status='Approve').count()
    pending = Application.objects.filter(status='Pending').count()
    reject = Application.objects.filter(status='Reject').count()
    if request.method == 'GET' :
        item_name = request.GET.get('table_search')
        if item_name != '' and item_name is not None:
            app = app.filter(Q(leave__icontains=item_name) | Q(status__icontains=item_name) | Q(pemohon__icontains=item_name))
            staff = staff.filter(Q(fullname__icontains = item_name))
    context = {
        'app' : app,
        'staff' : staff,
        'countstaff' : count,
        'approve' : approve,
        'pending' : pending,
        'reject' : reject
    }
    return render(request, 'core/index.html', context)
#----------------------------------------------------------------------------------------------------------

#Calendar directory --------------------------------------------------------------------------------------
@login_required
def calendar(request) :
    app = Application.objects.all()
    user = Staff.objects.all()
    context = {
        'user' : user,
        'appz' : app,
    }
    return render(request, 'core/calendar.html', context)
#------------------------------------------------------------------------------------------------------------

#staff list -------------------------------------------------------------------------------------------------
def staff(request) :
    user = Staff.objects.all()
    if request.method == 'GET' :
        item_name = request.GET.get('search')
        if item_name != '' and item_name is not None:
            user = user.filter(Q(fullname__icontains=item_name) | Q(cawangan__icontains=item_name) | Q(phone__icontains=item_name))
    context = {
        'staff' : user
    }
    return render(request, 'core/staff_profile.html', context)
#--------------------------------------------------------------------------------------------------------------

#To request apply form ------------------------------------------------------------------------------------
@login_required
def form(request):  
    staff = Staff.objects.all()
    if request.method == 'POST' :
        aform = ApplyLeaveForm(request.POST, request.FILES)
        if aform.is_valid() :
            aform.save()

            send_mail(
            'user',
            'hi, someone apply leave today, login to the system now',
            'mohdfitri525@gmail.com',
            ['mohdfitri1017@gmail.com'],
            )
            return redirect('dashboard')
    else:
        aform = ApplyLeaveForm()

    context = {
        'aform': aform,
        'staff' : staff,
    }
    return render(request, 'core/form.html', context)


#admin viewpage -------------------------------------------------------------------------------------------
def viewapp(request, pk) :
    app = Application.objects.get(id=pk)
    d0 = app.from_date
    d1 = app.to_date
    tot = d1 - d0 
    if request.method == 'POST' :
        form = Approval(request.POST, instance=app)      
        if form.is_valid() :
            form.save()
            return redirect('dashboard')
    else:
        form = Approval(instance=app)
    context = {
        'app' : app,
        'form' : form,
        'tot' : tot,
    }
    return render(request, 'core/view.html', context)
#-----------------------------------------------------------------------------------------------------


#history view page ----------------------------------------------------------------------------------------
def history_view(request, pk) :
    app = Application.objects.get(id=pk)
    d0 = app.from_date
    d1 = app.to_date
    tot = d1 - d0 
    context = {
        'app' : app,
        'tot' : tot
    }
    return render(request, 'core/history_view.html', context)

#history page
def history(request) :
    app = Application.objects.all()
    staff = Staff.objects.all()

    if request.method == 'GET' :
        item_name = request.GET.get('table_search')
        if item_name != '' and item_name is not None:
            app = app.filter(Q(leave__icontains=item_name) | Q(status__icontains=item_name) | Q(date_created__icontains=item_name) | Q(pemohon__icontains=item_name))
            staff = staff.filter(Q(fullname__icontains=item_name))
        
       

    context = {
        'app' : app,
        'staff' : staff
    }
    return render(request, 'core/history.html', context)

def pending(request) :
    app = Application.objects.all()
    staff = Staff.objects.all()

    if request.method == 'GET' :
        item_name = request.GET.get('table_search')
        if item_name != '' and item_name is not None:
            app = app.filter(Q(leave__icontains=item_name) | Q(status__icontains=item_name) | Q(date_created__icontains=item_name))
            staff = staff.filter(Q(fullname__icontains=item_name))
        
       

    context = {
        'app' : app,
        'staff' : staff
    }
    return render(request, 'core/pending.html', context)
#--------------------------------------------------------------------------------------------------------


#delete the items
@login_required()
def delete(request, pk):
   app = Application.objects.get(id=pk)
   if request.method == 'POST':
        app.delete()
        return redirect('dashboard')
   return render(request, 'core/delete.html')

#delete the staff
@login_required()
def staff_delete(request, pk):
   staff = Staff.objects.get(id=pk)
   if request.method == 'POST':
        staff.delete()
        return redirect('profile-staff')
   return render(request, 'core/staff_delete.html')


#staff view and edit items
@login_required()
def staff_view(request, pk):
    app = Application.objects.get(id=pk)
    if request.method == 'POST':
        form = ApplyLeaveForm(request.POST, request.FILES, instance=app)
        if form.is_valid():
           form.save()
           return redirect('dashboard')
    else:
        form = ApplyLeaveForm(instance=app)
    context = {
        'form': form,
        'app': app,
    }
    return render(request, 'core/staff_view.html', context)

@login_required
@permission_required('admin.can_add_log_entry')
def add_staff(request):

    if request.method == 'POST' :
        csv_file = request.FILES['file']     
        if not csv_file.name.endswith('.csv') :
            messages.error(request, 'This is not CSV file')
        
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar='|') :
            created = Staff.objects.update_or_create(
                fullname=column[0],
                email=column[1],
                phone=column[2],
                address=column[3],
                cawangan=column[4],
            )
        return redirect('dashboard')

    if request.method == 'POST' :
        form = AddStaff(request.POST, request.FILES)      
        if form.is_valid() :
            form.save()
            return redirect('dashboard')
    else:
        form = AddStaff()

    context = {
        'form' : form
    }

    return render(request, 'core/add_staff.html', context)


def staff_profile(request, pk) :
    staff = Staff.objects.get(id=pk)
    context = {
        'staff' : staff
    }
    return render(request, 'core/staff_details.html', context)

def edit_staff(request, pk) :
    staff = Staff.objects.get(id=pk)
    if request.method == 'POST' :
        uform = AddStaff(request.POST, request.FILES, instance=staff)
        eform = EditLeave(request.POST, instance=staff)
        if uform.is_valid() and eform.is_valid() :
            uform.save()
            eform.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile-staff')
    else:
        uform = AddStaff(instance=staff)
        eform = EditLeave(instance=staff)
    context = {
        'form' : uform,
        'eform': eform,
        'staff' : staff
    }
    
    return render(request, 'core/edit_staff_details.html', context)

#for print pdf ----------------------------------------------------------------------------------------------
def print(request, pk):
    app = Application.objects.get(id=pk)
    role = Role.objects.all()
    template_path = 'core/print.html'
    context = {
        'app': app,
        'role': role,

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
     # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
     # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
#--------------------------------------------------------------------------------------------------------------


#import data from database ----------------------------------------------------------------------------------
def getdata(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="staff.csv"'  
    employees = Staff.objects.all()  
    writer = csv.writer(response)  
    for employee in employees:  
        writer.writerow([employee.fullname,employee.email,employee.phone, employee.address, employee.cawangan])  
    return response  


#------------------------------------------------------------------------------------------------------------
    