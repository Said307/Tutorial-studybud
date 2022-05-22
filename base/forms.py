from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm

from .models import *

from django.contrib.auth import get_user_model


class RoomForm(ModelForm):
    class Meta:
        model = Room  # Table name
        exclude = ["participants", "host"]


class MyUserCreationForm(
    UserCreationForm
):  # registration for has different parent than update form
    class Meta:
        model = get_user_model()
        fields = ["name", "username", "email", "password1", "password2"]


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "avatar", "bio"]
