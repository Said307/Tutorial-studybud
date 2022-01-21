from django.shortcuts import render, HttpResponse

# Create your views here.



def home(request):

    return render(request,'base/home.html')




def room(request,pk):

    context = {'id':pk}

    return render(request,'base/room.html',context)