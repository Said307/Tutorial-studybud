



from django.forms import ModelForm

from . models import *

from django.contrib.auth import get_user_model




class RoomForm(ModelForm):

    class Meta :
        model = Room     # Table name
        exclude = ['participants','host']





class ProfileForm(ModelForm):

    class Meta :
        model =  get_user_model()
        fields = ['username','email','password','bio']
