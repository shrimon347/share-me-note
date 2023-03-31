
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Room



class CreateUserForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'input'}))
    # first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'First name','class':'login__input'}))
    # last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Last name','class':'login__input'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2',]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)


        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'input'


        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'input'

        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].widget.attrs['class'] = 'input'


class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

