from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .filters import SearchFilter
import account
from django.contrib import messages
from .forms import RegisterForm,BlogForm,UpdateForm,ChangeForm

from .models import employee_database,blogpost
from django.contrib.auth import authenticate,login,logout

from account import forms
# Create your views here.

def home(request):
    current_user = request.user
    user_id = current_user.username
    print(user_id)
    f = employee_database.objects.all()
    return render(request,'index.html')

def wrong_dat_fetch(request):
    return HttpResponse("You filled the wrong entry !!") 

def New_user_register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('user_login')
            else:
                return HttpResponse('<div style="color:red; text-align: center;"><h2>You enter the wrong filled. Please Check Again and submit..!!</h2></div><br><a href="new_user_register">Back</a>')

        except:
            return redirect("/")

    else:
        context = {'data':RegisterForm}
        return render(request,'register.html',context)




def User_login(request):
    username = "not logged in"
    if request.method=='POST':
        request.session['username']=username
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        
        try:
            if passw and uname is None:
                return redirect("user_login")
            else:

                user = authenticate(request, username=uname, password=passw)
                if user is not None:
                    print(uname,passw)
                    login(request,user)
                    return redirect("/")
                else:
                    return HttpResponse("<div style='color:red; text-align: center;'><h2>Invalid Username and Password.!!</h2></div>")
        except:
            return redirect("/")

    else:
        return render(request,'login.html')


def Userlogout(request):
    logout(request)
    return redirect("user_login")


'''
def UserInfo(request):
    current_user = request.session['username']
    user  = current_user
    print(user)
    emp = employee_database.objects.filter(username=user) 
    return render(request,'userinfo.html', {'user':emp})'''

#account
def UserUpdate(request):
    username = request.user
    print(username)
    empdata = employee_database.objects.filter(username=username)
    blogdata = NewBlog.objects.all()
    return render(request,'useraccount.html',{'userdata':username,'empdata':empdata,'new_post':blogdata})    

#userlist
def users_data(request):
    emp = employee_database.objects.all()
    myFilter = SearchFilter(request.GET, queryset=emp)
    emp = myFilter.qs
    user_count = emp.count()
    context = {'data':emp,'filters':myFilter,'count':user_count}
    return render(request,'userslist.html',context)

#accountupdate
def editinfo(request,id):
    eid = employee_database.objects.get(id=id)
    #newpost = NewBlog.objects.all()
    if request.method=="POST":
        form = RegisterForm(request.POST,request.FILES,instance = eid)
        try:
            if form.is_valid():
                form.save()
                return redirect('/')
        except Exception:
            return HttpResponseRedirect('unsaved/user_login')
    else:
        et = RegisterForm(instance=eid)
        context = {'data':et}
        return render(request,'register.html',context)

#updateuser

def useredit(request,id):
    uid = employee_database.objects.get(id=id)
    if request.method=="POST":
        form = UpdateForm(request.POST, request.FILES, instance=uid)
        form.save()
        return redirect('userslist')
    else:
        et = UpdateForm(instance=uid)
        context = {'data':et}
        return render(request,'update.html',context)

#delete user
def remove_user(request,id):
    form  = employee_database.objects.get(id=id)
    form.delete()
    return redirect("userslist")

#updatephotot
def UpdatePhoto(request,id):
    eid = employee_database.objects.get(id=id)
    if request.method=="POST":
        form = ChangeForm(request.POST, request.FILES, instance = eid)
        form.save()
        return redirect("/") 
    else:
        
        context = {'form':ChangeForm}
        return render(request,'changeprofile.html',context)




from filterdata.models import NewBlog,blogform
# Create your views here.
#blogccreate
def createblog(request):
    if request.method=="POST":
        form = blogform(request.POST, request.FILES)
        form.save()
        return redirect("/")
    else:
        return render(request,'createblog.html',{'blog':blogform})

#view blog
def blogView(request):
    data = NewBlog.objects.all()
    context = {'blog':data}
    return render(request,'blogTemplate.html',context)

#previews blog
def blog_preview(request,id):
    user  = NewBlog.objects.filter(id=id)
    print(user)
    context ={'data':user}
    return render(request,'blogreviews.html',context)

#export data
import csv
def check(request):
    return render(request,'download.html')


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']= 'attachment; filename="users.csv"'

    write = csv.writer(response)
    write.writerow(['first_name','last_name','email','username','phone no','city','gender','job_profile','report_manager','DOB','date_joining'])

    users =  employee_database.objects.all().values_list('first_name','last_name','email','username','phone','city','gender','job_profile','report_manager','date_of_birth','date_joined')
    for user in users:
        write.writerow(user)

    return response
