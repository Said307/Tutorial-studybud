from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from ..models import *
from .serializers import *


@api_view(["GET"])  # only accepts a GET request.
def getRoutes(request):

    routes = [
        "GET api/rooms",
        "GET api/rooms/:name",
    ]

    return Response(routes)


@api_view(["GET"])
def getRooms(request):

    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getRoom(request, roomname):

    room = Room.objects.get(name=roomname)
    serializer = RoomSerializer(room)
    return Response(serializer.data)
