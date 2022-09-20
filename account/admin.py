from dataclasses import field
from django.contrib import admin
from import_export.admin  import ImportExportModelAdmin
from import_export import resources
from .models import employee_database,blogpost



class EmployeeResource(resources.ModelResource):
    class Meta:
        model = employee_database
        import_id_field = ('id',)
        fields = ('id','first_name','last_name','phone','email','gender','date_of_birth','city','job_profile','report_manager','username',)

class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    list_display = ('first_name','last_name','phone','email','is_superuser')
    list_filter = ('city','job_profile',)


admin.site.register(employee_database,EmployeeAdmin)




class BlogAdmin(admin.ModelAdmin):
    fields = ('title','description','image',)
    list_display =('title',)

admin.site.register(blogpost, BlogAdmin)

