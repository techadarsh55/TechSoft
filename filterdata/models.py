from dataclasses import fields
from email import header
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NewBlog(models.Model):
    
    title  = models.CharField(max_length=350,blank=False,default='title')
    descriptions = models.TextField(max_length=5000, blank=False)
    blog_image  = models.ImageField(default="",upload_to="NewBlog")
    posttime = models.DateField(blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django import forms 

class blogform(forms.ModelForm):
    class Meta:
        model = NewBlog
        fields = ['title','descriptions','blog_image','posttime','user']

        widgets = {

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'blog tilte','required':'required'}),
            'descriptions':forms.Textarea(attrs={'class':'form-control','placeholder':'blog Description...'}),
            'blog_image':forms.FileInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
            'posttime':forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
        }
        
        def userid(self, request):
            user = request.user
            data = NewBlog.objects.filter(username=user)
            return user


