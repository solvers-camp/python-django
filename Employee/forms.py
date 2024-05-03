from django import forms
from Employee.models import Employee
from Department.models import Department

class EmployeeForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('', '---------'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ['name', 'contact', 'email', 'gender', 'address', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
