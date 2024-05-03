from Employee.models import Employee
from django.test import RequestFactory
from pytest import mark
from Employee.views import addnew,index,destroy, edit, update
from django.urls import reverse

@mark.django_db
def test_addnew_view_post():
    factory = RequestFactory()
    request = factory.post('/addnew/')
    response = addnew(request)
    assert response.status_code == 200

@mark.django_db
def test_addnew_view_get():
    factory = RequestFactory()
    request = factory.get('/addnew/')
    response = addnew(request)
    assert response.status_code == 200

@mark.django_db
def test_index_view():

    factory = RequestFactory()
    request = factory.get('/')
    response = index(request)

    assert response.status_code == 200

@mark.django_db
def test_edit_view():
    # Create a sample employee
    employee = Employee.objects.create(name="John Doe")

    factory = RequestFactory()
    request = factory.get(reverse('edit', kwargs={'id': employee.id}))
    response = edit(request, employee.id)

    assert response.status_code == 200 
    
@mark.django_db
def test_update_view():
    # Create a sample employee
    employee = Employee.objects.create(name="John Doe")

    factory = RequestFactory()
    post_data = {'name': 'employee-update'} 
    request = factory.post(reverse('employee-update', kwargs={'id': employee.id}), data=post_data)
    response = update(request, employee.id)

    assert response.status_code == 200

@mark.django_db
def test_destroy_view():
    # Create a sample employee
    employee = Employee.objects.create(name="John Doe")

    # Get the initial count of employees
    initial_employee_count = Employee.objects.count()

    # Create a mock request
    factory = RequestFactory()
    request = factory.get(reverse('destroy', kwargs={'id': employee.id}))

    # Call the destroy view function with the mock request
    response = destroy(request, id=employee.id)

    # Get the final count of employees after deletion
    final_employee_count = Employee.objects.count()

    assert response.status_code == 302
    assert response.url == reverse('index')
    assert final_employee_count == initial_employee_count - 1  
