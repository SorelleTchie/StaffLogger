from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, CheckInOutForm
from .models import Employee, AttendanceRecord
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
import os, logging 


def landing_page(request):
    records = AttendanceRecord.objects.all()
    return render(request,"landing_page.html", {'records':records})

def new_employees(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            # Query the database using the primary key of the new instance
            employee_in_db = Employee.objects.filter(pk=employee.pk).first()
            if employee_in_db:
                #The new instance has been saved to the database
                return redirect('new_employees')
            else:
                #The new instance was not saved to the database 
                return render(request, 'error.html', {'message': 'Failed to save employee'})

    else:
        form = EmployeeForm()
    return render(request, 'new_employees.html', {'form': form})


def check_in(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        record = AttendanceRecord.objects.create(employee=employee, check_in_time=timezone.now())
        return render(request, 'checked_in.html', {'employee': employee,'record': record})
    return render(request, 'check_in.html')  
    
    
def check_out(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        attendance = AttendanceRecord.objects.filter(employee=employee, check_out_time__isnull=True).last()
        if attendance:
            attendance.check_out()
        return render(request, 'checked_out.html', {'employee': employee, 'attendance':attendance})
    return render(request, 'check_out.html')
