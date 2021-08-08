from django import forms
from django.forms import fields, widgets
from .models import Resume

GENDER_CHOICES = [
    {'Male', 'Male'},
    {'Female', 'Female'}
    # {'Other', 'Other'}
]

class ResumeForm(forms.ModelForm):
    
    class Meta:
        model = Resume
        fields = ['name','profile_img','about','dob','gender','email','state','clg','degree','grades','role','company','exp','proj','link','certificate','organisation','interest']
        labels = {'name': 'Full Name', 'profile_img':'Profile Image', 'about': 'About Yourself', 'dob': 'Date of Birth','gender':'Gender','email': 'Email ID','state':'State','clg':'College Name', 'degree':'Degree', 'grades':'Grades', 'role':'Work Experience/Role','company':'Company Name','exp':'Experience (in months/years)','proj':'Project Name', 'link':'Link', 'certificate':'Certificate Name', 'organisation':'Organisation Name', 'interest': 'Stae your Interests'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'about':forms.Textarea(attrs={'class':'form-control'}),
            'profile_img':forms.FileInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker', 'type':'date'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'clg': forms.TextInput(attrs={'class':'form-control'}),
            'degree': forms.TextInput(attrs={'class':'form-control'}),
            'grades': forms.TextInput(attrs={'class':'form-control'}),
            'role': forms.TextInput(attrs={'class':'form-control'}),
            'company': forms.TextInput(attrs={'class':'form-control'}),
            'exp':forms.TextInput(attrs={'class':'form-control'}),
            'proj':forms.TextInput(attrs={'class':'form-control'}),
            'link':forms.TextInput(attrs={'class':'form-control'}),
            'certificate':forms.TextInput(attrs={'class':'form-control'}),
            'organisation':forms.TextInput(attrs={'class':'form-control'}),
            'interest':forms.Textarea(attrs={'class':'form-control'}),
            
        }