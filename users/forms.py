from django import forms

from .models import CustomeUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomeUser
        fields = ('first_name', 'last_name', 'email', 'username',)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomeUser
        fields = ('first_name', 'last_name', 'username', 'email', 'tg_username', 'avatar', 'phone_number',)