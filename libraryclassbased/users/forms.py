from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from users.models import CustomUser
# class SignupForm(UserCreationForm):
#     gender_choices=(('Male','Male'),('Female','Female'))
#     gender=forms.CharField(choices=gender_choices,widget=forms.RadioSelect)
#
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','email','first_name','last_name','password2']





# class Meta:
#        model=CustomUser
#        field=['username','password1','password2','gender','email','first_name','last_name','phone','address']





class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)














