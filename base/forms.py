



from django.forms import ModelForm

from . models import *





class RoomForm(ModelForm):

    class Meta :
        model = Room     # Table name
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

