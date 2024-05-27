from .models import student,studSignup,StudentFile
from django import forms
from django.forms import TextInput,EmailInput


class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='name','course','email'
        widgets={
            'name': forms.TextInput(attrs={'class':'form-field'}),
            'course':forms.TextInput(attrs={'class':'form-field'}),
            'email':forms.EmailInput(attrs={'class':'form-field'}),
        }


from django import forms
from .models import studSignup

class studSignupform(forms.ModelForm):
    class Meta:
        model = studSignup
        fields = ('f_name', 'l_name', 'd_o_b', 'id_number', 'course', 'email')
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-field'}),
            'l_name': forms.TextInput(attrs={'class': 'form-field'}),
            'd_o_b': forms.DateInput(attrs={'class': 'form-field'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-field'}),
            'course': forms.TextInput(attrs={'class': 'form-field'}),
            'email': forms.EmailInput(attrs={'class': 'form-field'}),
        }


class studentFileForm(forms.ModelForm):
    class Meta:
        model=StudentFile
        fields = '__all__'
        widgets = {
            'emial':forms.TextInput(attrs={}),
            'certificate':forms.FileInput(), 
        }



        