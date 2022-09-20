from django import forms
from .models import employee_database,blogpost
from django.contrib.auth.forms import UserCreationForm

from account import models


class RegisterForm(UserCreationForm):
    class Meta:
        model = employee_database
        fields = ['first_name','last_name','phone','email','gender','date_of_birth','city','date_joined','job_profile','report_manager','avatar','username','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','label':'First Name','required': 'required'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','label':'Last Name','required':'required'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','label':'Phone','required':'required','minlength':'10','pattern':'[1-9]{1}[0-9]{9}','placeholder':'Enter 10 digit number.'}),
            'email':forms.EmailInput(attrs={'class':'form-control','label':'Email','required':'required','pattern':'[a-z].[a-z].+@techsoft\.com','placeholder':'your.mail@techsoft.com'}),
            'gender':forms.Select(attrs={'class':'form-control','label':'Gender','required':'required'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control','label':'Date Of Birth','placeholder':'YYYY-MM-DD'}),
            'city':forms.TextInput(attrs={'class':'form-control','label':'Area & City','required':'required'}),
            'date_joined':forms.DateTimeInput(attrs={'class':'form-control','label':'Date Of Joined'}),
            'job_profile':forms.TextInput(attrs={'class':'form-control','required':'required'}),
            'report_manager':forms.TextInput(attrs={'class':'form-control',}),
            'avatar':forms.FileInput(attrs={'class':'form-control','required':'required'}),
            'username':forms.TextInput(attrs={'class':'form-control','required': 'required'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','minlength':'8'})
           

        }


class ChangeForm(forms.ModelForm):
    model = employee_database
    fields = ['user','image']
    widgets = {
        'user':forms.TextInput(attrs={'class':'form-control','required': 'required'}),
        'image':forms.FileInput(attrs={'class':'form-control','required':'required'}),

    }

class BlogForm(forms.ModelForm):
    class Meta:
        model = blogpost
        fields = ["title","description","image",]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'blog tilte','required':'required'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'blog Description...'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }
        

class UpdateForm(forms.ModelForm):
    class Meta:
        model = employee_database
        fields = ['first_name','last_name','phone','email','gender','date_of_birth','city','date_joined','job_profile','report_manager','username']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control','label':'First Name','required': 'required'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','label':'Last Name','required':'required'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','label':'Phone','required':'required','minlength':'10','pattern':'[1-9]{1}[0-9]{9}','placeholder':'Enter 10 digit number.'}),
            'email':forms.EmailInput(attrs={'class':'form-control','label':'Email','required':'required','pattern':'[a-z].[a-z].+@techsoft\.com','placeholder':'your.mail@techsoft.com'}),
            'gender':forms.Select(attrs={'class':'form-control','label':'Gender','required':'required'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control','label':'Date Of Birth','placeholder':'YYYY-MM-DD'}),
            'city':forms.TextInput(attrs={'class':'form-control','label':'Area & City','required':'required'}),
            'date_joined':forms.DateTimeInput(attrs={'class':'form-control','label':'Date Of Joined'}),
            'job_profile':forms.TextInput(attrs={'class':'form-control','required':'required'}),
            'report_manager':forms.TextInput(attrs={'class':'form-control',}),
            'username':forms.TextInput(attrs={'class':'form-control','required': 'required'}),
    

        }