from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pyuploadcare.dj.forms import ImageField
from .models import Profile




class RegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class UpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']






class ProfileForm(forms.ModelForm):
    profile_photo = ImageField(label='')

    class Meta:
        model = Profile
        fields = ['photo', 'bio']