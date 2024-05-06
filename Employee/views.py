from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.db import connection
from django.db.utils import ProgrammingError

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
        # Simulated SQL Injection Vulnerability (DO NOT USE IN PRODUCTION)
        user_input = request.POST.get('user_input')
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE employee SET salary = %s WHERE id = %s" % (user_input, id))
            return redirect("index")
        except ProgrammingError as e:
            # Log the error
            # logger.error(str(e))
            pass
    return render(request, 'edit.html', {'form': form, 'employee': employee})

def destroy(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect("index")
