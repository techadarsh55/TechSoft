from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


GENDER_CHOICE = (
    ('select','Select'),
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Others'),

)


class employee_database(User):
    
    phone = models.CharField(max_length=10,blank=False,validators=[RegexValidator(regex='^[0-9]{10}$', message="Please enter the 10 digit number")],default='')
    date_of_birth = models.DateField(max_length=11, blank=False, null=False,help_text="Date format: YYYY-MM-DD")
    job_profile = models.CharField(max_length=150, blank=False, null=False)
    report_manager = models.CharField(max_length=50,  blank=True, null=True)
    avatar = models.ImageField(blank=False, upload_to ='user_profile',default="")
    gender = models.CharField(max_length=15,choices=GENDER_CHOICE, blank=False, default='Select', null=False)
    city = models.CharField(max_length=150,blank=True, null=True) 


    class Meta:
        db_table = "register_data"

    def  __str__(self):
        return self.email


class blogpost(models.Model):
    title = models.CharField(max_length=500)
    description  = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="Blog", default="")
    posttime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "blog"

    def __str__(self):
        return self.title





