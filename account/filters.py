from django import forms
import django_filters
from .models import employee_database
class SearchFilter(django_filters.FilterSet):

    class Meta:
        model = employee_database
        fields = {'first_name':['icontains'],'email':['icontains'],'phone':['exact'],'job_profile':['icontains'],'city':['icontains']}
        