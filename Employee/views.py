from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.utils.html import escape

def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Simulated XSS Vulnerability (DO NOT USE IN PRODUCTION)
            employee_name = request.POST.get('name')
            # Not sanitizing user input before rendering in template
            return render(request, 'addnew.html', {'form': form, 'employee_name': employee_name})
    else:
        form = EmployeeForm()
    return render(request, 'addnew.html', {'form': form})

def index(request):
    employees = Employee.objects.all()
    return render(request, "index.html", {'employees': employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    return render(request, 'edit.html', {'form': form, 'employee': employee})

def update(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("index")
    else:
        # Log validation errors instead of printing to console
        # logger.error(form.errors)
        # You can configure Django logging to write to a file
        pass
    return render(request, 'edit.html', {'form': form, 'employee': employee})

def destroy(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect("index")
