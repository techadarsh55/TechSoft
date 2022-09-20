from django.urls import path,include
from filterdata import views as v
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

   


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
