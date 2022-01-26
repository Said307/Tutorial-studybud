from django.shortcuts import render, HttpResponse,redirect

from . models import *
from . forms import *
# Create your views here.



def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)




def room(request,url2):

    room = Room.objects.get(name=url2)
    context = {'room':room}

    return render(request,'base/room.html',context)


def create_room(request):

    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render(request,'base/room_form.html',context)



def update_room(request,url2):
    room = Room.objects.get(name=url2)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form,'room':room}
    return render(request,'base/room_form.html',context)




def delete_room(request,url2):
    room = Room.objects.get(name=url2)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'room':room}
    return render(request,'base/delete.html',context)

