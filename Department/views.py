from django.shortcuts import render, redirect
from Department.forms import DepartmentForm
from Department.models import Department

# Create your views here.
def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department-list')
    else:
        form = DepartmentForm()
    return render(request, 'department_create.html', {'form': form})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_show.html', {'departments': departments})

def department_edit(request, id):  
    department = Department.objects.get(id=id)  
    return render(request,'department_edit.html', {'department':department})  
 
def department_update(request, id):  
    department = Department.objects.get(id=id)  
    form = DepartmentForm(request.POST, instance = department)  
    if form.is_valid():  
        form.save()  
        return redirect("department-list")  
    return render(request, 'department_edit.html', {'department': department})  

def department_destroy(request, id):  
    department = Department.objects.get(id=id)  
    department.delete()  
    return redirect("department-list")
