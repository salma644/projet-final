from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userlist



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
        widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'type' :'text', 'id' : 'username'}))
    password = forms.CharField(label="Password", max_length=30,
        widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'type' :'password', 'id' : 'password'}))

class MyForm(forms.Form):
    my_object = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
    )
    

