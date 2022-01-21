from django.shortcuts import render, HttpResponse

# Create your views here.



def home(request):

    return HttpResponse('Welcome Home')




def room(request):

    return HttpResponse('Room 1')