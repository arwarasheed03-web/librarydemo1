from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render,redirect

# def register(request):
#     return HttpResponse("Register")
# def userlogin(request):
#     return HttpResponse("Login")
# def userlogout(request):
#     return HttpResponse("Logout")

# def register(request):
#     return render(request,'register.html')
from django.views import View

from users.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm

from users.forms import LoginForm


class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST,request.FILES)
        if form_instance.is_valid():

            form_instance.save()
            return redirect('users:userlogin')

    def get(self, request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)

# def userlogin(request):
#     return render(request,'userlogin.html')

from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
class Userlogin(View):
        def post(self, request):
            form_instance = LoginForm(request.POST)
            if form_instance.is_valid():
                data=form_instance.cleaned_data
                print(data)
                u=data['username'] #reads the username from cleaned data and assigns to variable u
                p=data['password'] #reads the password from cleaned data and assigns to variable p
                                   # authentication/login/logout--built in functions defined inside contrib.aith module
                user=authenticate(username=u,password=p)
                        #authenticate() checks whether a user record exists in the user table
                        #matching with the submitted username and password,if yes,it returns the
                        #user object else it returns none.
                if user: #if user already exists...
                    login(request,user) #adds the user into current session
                    return redirect('books:home') #redirects to home page
                else: #if user does not exists...
                    messages.error(request,"Invalid user credentials")
                    return redirect('users:userlogin')

        def get(self,request):
            form_instance=LoginForm()
            context={'form':form_instance}
            return render(request,"userlogin.html",context)
#
# #
# def userlogout(request):
#     return redirect("users:userlogin")
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('users:userlogin')

    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'userlogin.html',context)

class Userlogout(View):
    def get(self,request):

        logout(request) #removes the logged user from the current session
        return redirect("users:userlogin")