from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserLoginForm, ChatRoomForm
from .models import ChatRoom
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'index.html', {'chat_rooms': chat_rooms})

@login_required
def create_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.save()
            chat_room.members.add(request.user)
            return redirect('chat_room', room_id=chat_room.id)
    else:
        form = ChatRoomForm()
    return render(request, 'create_chat_room.html', {'form': form})

@login_required
def chat_room(request, room_id):
    chat_room = ChatRoom.objects.get(id=room_id)
    return render(request, 'chat_room.html', {'chat_room': chat_room})

@login_required
def delete_chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    if request.method == 'POST':
        room.delete()
        return redirect('index')
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})