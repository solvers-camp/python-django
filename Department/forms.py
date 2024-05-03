from django import forms
from Department.models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department', 'head_of_department', 'number_of_staff', 'contact_phone', 'contact_email']
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'head_of_department': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_staff': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
