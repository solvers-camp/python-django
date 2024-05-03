from django.db import models
from Department.models import Department

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100) 
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, default=None)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
   
    class Meta:  
        db_table = "Employee_Table"
