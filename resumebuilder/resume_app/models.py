from django.db import models

STATE_CHOICE = (
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),
    ("Lakshadweep","Lakshadweep"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Puducherry","Puducherry"),

)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)
# Create your models here.

class Resume(models.Model):
    name = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profileimg', blank = True)
    about = models.CharField(max_length=200, default="")
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100)
    email = models.EmailField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    clg = models.CharField(max_length=100, default="")
    degree = models.CharField(max_length=100, default="")
    grades = models.CharField(max_length=100, default="")
    role = models.CharField(max_length=100, default="")
    company = models.CharField(max_length=100, default="")
    exp = models.CharField(max_length=100, default="")
    proj = models.CharField(max_length=100, default="")
    link = models.CharField(max_length=100, default="")
    certificate = models.CharField(max_length=100, default="")
    organisation = models.CharField(max_length=100, default="")
    interest = models.CharField(max_length=200, default="")