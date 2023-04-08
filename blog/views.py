from django.shortcuts import render
from .models import Room
from .forms import RoomForm

# Create your views here.
# rooms=[
    
#     {'id':1, 'name':"let's Learn Python"},
#     {'id':2, 'name':"let's Learn Javascript"},
#     {'id':3, 'name':"let's Learn Web Development"},
#     {'id':4, 'name':"let's Learn Data Science"},
# ]


def home(request):
    rooms= Room.objects.all()
    context={'rooms':rooms}
    return render(request, 'blog/home.html', context)

def room(request, pk):
    room=Room.objects.get(id=pk)
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room=i
    context={'room': room}
    return render(request, 'blog/room.html', context)


def createRoom(request):
    return render(request,'blog/form_register.html' )


