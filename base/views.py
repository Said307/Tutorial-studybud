from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . models import *
from . forms import *
# pagination
from django.core.paginator import Paginator



def home(request):
    # Home isplays filtered  database objects.
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # | pipe means OR
    """rooms = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)
          # table name __ fieldname

    )"""

    rooms = Room.objects.all()
    topics = Topic.objects.all()

    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q) #if the room's topic's name conatains q


    )[:6]

    #Set up pagination
    paginator = Paginator(rooms, 5)
    page_number  = request.GET.get('page',1)
    page_obj = paginator.page(page_number)
    context = {'topics':topics,'rooms':rooms,'room_messages':room_messages,'movies':page_obj}
    return render(request,'base/home.html',context)





def room(request,url2):

    room = Room.objects.get(name=url2)
    participants = room.participants.all()
    room_messages = room.message_set.all()
    # create a new message
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            body = request.POST.get('body'),
            room = room
            )
        #When a user enters this room add his name to the room.participants list
        room.participants.add(request.user)
        redirect('room',url2=room.name)


    context = {'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)



#======================ROOM CRUD ===================================

@login_required(login_url='/login')    # redirecting to unauthorized users login page
def create_room(request):

    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.host =request.user
            obj.save()
            return redirect('home')

    context = {'form':form}

    return render(request,'base/room-form.html',context)



def update_room(request,url2):
    room = Room.objects.get(name=url2)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return redirect('login')
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form,'room':room}
    return render(request,'base/room-form.html',context)




def delete_room(request,url2):
    room = Room.objects.get(name=url2)
    if request.user != room.host:
        return redirect('login')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request,'base/delete.html',context)



#==============User login system=====================

def register(request):
    #step 1 capture new user details
    page = 'register'

    form = UserCreationForm()
    #step 2 save user details on the User database tabel
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # fill the form with POST data
        if form.is_valid():
            user = form.save(commit=False)       # don't save it in database yet
            user.username =user.username.lower()
            user.save()   # Now, save it on the database
            login(request,user)                  # login the new user straight away
            return redirect('home')
        else:
            messages.error(request,'Registration error')

    context = {'page':page,'form':form}
    return render(request,'base/login_register.html',context)


def login_page(request):
    """ This view can show login OR register template"""

    page  = 'login'
    """ manual process instad of using modelform """
    #step 1a check if user is already logged in
    if request.user.is_authenticated:
        return redirect('home')
    # step 1, check if user is in database
    if request.method == 'POST':
        username  = request.POST.get('username').lower()
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
    context = {'page':page}
    return render(request,'base/login_register.html',context)



def logout_page(request):

    logout(request)

    return redirect('home')



#======================message CRUD=================================

def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('No permission')
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    context = {'obj':message}
    return render(request,'base/delete.html',context)



#======================User Profile=================================


def profile(request,name):

    user =  get_object_or_404(User,username=name)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user':user,'rooms':rooms,'topics':topics,'room_messages':room_messages}
    return render(request,'base/profile.html',context)



