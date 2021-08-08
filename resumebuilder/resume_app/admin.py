from django.contrib import admin
from .models import Resume
# Register your models here.

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','profile_img','about','dob','gender','email','state','clg','degree','grades','role','company','exp','proj','link','certificate','organisation','interest']