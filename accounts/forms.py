from tkinter.ttk import Style
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import fields
from . models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'placeholder' : 'Talk a little about you', 'rows': 10}
                                 ),
                                 )
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(
                                attrs={'class':'latname_input'}
                                 ),
                                 )
    instagram_link = forms.CharField(max_length=200)
    phone_link = forms.CharField(max_length=200)
    email = forms.EmailField()
    # username = forms.CharField(max_length=100,
    #                             widget=forms.TextInput(
    #                             attrs={'class':'form-group'}
    #                              ),
    #                              )
    

    class Meta:
        model = User
        fields = "__all__"
        fields =  ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','password2']
        help_texts = {
            'username': None,
            'email': None,
            'password2':None,
        }
   
               

    

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields =  ['username', 'first_name', 'last_name',    'email', ]
        help_texts = {
            'username': None,
            'email': None,
            
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image_url']
        
        
        
        
        
        