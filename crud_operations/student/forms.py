from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name", "email", "password")
        # fields = '__all__'   # Show all fields in form
        # exclude= ['name']  # Exclude field from form
        widgets = {
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name', 'class': 'form-control'}) ,
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email',}),
        }