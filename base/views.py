from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from . models import *
from . forms import *
# Create your views here.



def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # | pipe means OR
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(message__body__icontains=q)  # table name __ fieldname

    )


    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'topics':topics,'rooms':rooms}

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


#==============User login system=================

def register(request):

    context = {}
    return render(request,'base/register.html',context)


def login_page(request):

    """ manual process instad of using modelform """

    # step 1, check if user is in database
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User not found')
        # step 2, check if the user's credenials are correct
        user = authenticate(request,username=username,password=password)
        #step 3, give access, and add user to the session database
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Incorrect password')
    context = {}
    return render(request,'base/login.html',context)


def logout_page(request):

    logout(request)

    return redirect('home')










