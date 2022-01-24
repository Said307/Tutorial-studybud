from django.shortcuts import render, HttpResponse

from . models import *
# Create your views here.



def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)




def room(request,pk):

    room = Room.objects.get(id=pk)
    context = {'id':pk}

    return render(request,'base/room.html',context)