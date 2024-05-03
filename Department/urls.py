from django.urls import path
from Department import views

urlpatterns = [
    path('', views.department_list, name='department-list'),
    path('add', views.department_create, name='department-create'),
    path('edit/<int:id>', views.department_edit, name='department-edit'),
    path('update/<int:id>', views.department_update, name='department-update'),
    path('delete/<int:id>', views.department_destroy, name='department-delete'),
]
