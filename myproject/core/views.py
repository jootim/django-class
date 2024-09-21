from django.shortcuts import render, redirect
from .models import Room, Toppic

from .form import RoomForm
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# rooms = [
#     {'id':1,'name':'Web Develobment!'},
#     {'id':2,'name':'Backend Professional'},
#     {'id':3,'name':'Native application Rocks!'},
# ]


def core(request):
    return render(request, "base/home.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user is not registered")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password is not correct")
    context = {}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    topics = Toppic.objects.all()
    room_count = rooms.count()
    if request.user.is_authenticated:
        current_user = request.user
    context = {
        "rooms": rooms,
        "topics": topics,
        "q": q,
        "room_count": room_count,
    }
    # return render(request, "base/home.html", context)
    return render(request, "base/demo_2/index.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, "base/room.html", {"room": room})


@login_required(login_url="login")
def createroom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            start_save = form.save()
            start_save.user = request.user
            start_save.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.user:
        return HttpResponse("You are not allowed to to that!")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="login")
def deleteroom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")

    if request.user != room.user:
        return HttpResponse("You are not allowed to to delete the room!")

    return render(request, "base/delete.html", {"obj": room})


def lobby(request):
    return render(request, "base/demo_2/index.html")
