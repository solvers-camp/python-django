from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee

def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'addnew.html', {'form': form})

def index(request):
    employees = Employee.objects.all()
    return render(request, "index.html", {'employees': employees})

def edit(request, id):
    employee = get_object_or_404(Employee, id=id)
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
