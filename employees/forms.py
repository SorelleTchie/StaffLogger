from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'department', 'email']

class CheckInOutForm(forms.Form):
    employee_id = forms.IntegerField(
        label='Employee ID',
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Employee ID'})
    )