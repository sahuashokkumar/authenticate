from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import Signupform
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,"testapp/home.html")
@login_required
def python_view(request):
    return render(request,"testapp/python.html")
@login_required
def java_view(request):
    return render(request,"testapp/java.html")
@login_required
def aptitude_view(request):
    return render(request,"testapp/aptitude.html")
def logout_view(request):
    return render(request,"testapp/logout.html")

def signup_view(request):
    form=Signupform()
    if request.method=='POST':
        form=Signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,"testapp/signup.html",{'form':form})
