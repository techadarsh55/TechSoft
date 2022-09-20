from django.contrib import admin
from .models  import NewBlog

class blogAdmin(admin.ModelAdmin):
    list_display = ('title','user',)


admin.site.register(NewBlog,blogAdmin)