from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1','password2']



class Bookupdate(ModelForm):
    class Meta:
        model = Book
        fields = ['book_name','author_name','pic','status']



class Bookborrow(ModelForm):
    class Meta:
        model = Borrow
        fields = ['user','book','book_return']
