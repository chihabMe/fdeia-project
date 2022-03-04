from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={"class":"form-input form-user"}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"form-input form-pass"}))



class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={"class":"form-input form-user"}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"form-input form-pass"}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"form-input form-pass"}))


    class Meta :    
        model = User 
        fields=['username','password1','password2']

    


    
