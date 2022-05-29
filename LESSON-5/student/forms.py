from dataclasses import field
from django import forms
from .models import Student


class StudentFormSimple(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.IntegerField(required=False)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        field = '__all__'
