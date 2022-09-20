from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from account import views
from filterdata import views as v




urlpatterns = [
    path('', views.home,name="home"),
    
    path('new_user_register',views.New_user_register,name="new_user_register"),
    path('user_login',views.User_login,name="user_login"),
    path('user_logout',views.Userlogout,name='user_logout'),
    path('userslist',views.users_data,name="userslist"),
    path('user_home',views.UserUpdate,name='user_home'),
    path('edit/<int:id>',views.editinfo),
    path('imgedit/<int:id>',views.UpdatePhoto),
    path('edituser/<int:id>',views.useredit),
    path('deleteuser/<int:id>',views.remove_user),

    path('create_blog',views.createblog,name='create_blog'),
    path('see_all',views.blogView,name="see_all"),
    path('view_blog_page/<int:id>',views.blog_preview),
    path('export_data_csv',views.export_users_csv),
    path('download',views.check),

    


      


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
