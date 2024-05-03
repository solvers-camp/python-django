from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)
    number_of_staff = models.IntegerField()
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()

    def __str__(self):
        return self.department

    class Meta:  
        db_table = "Department_Table"
