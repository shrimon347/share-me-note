from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from .models import Room,Topic,Message,Notes,Chat
from datetime import date
from .forms import RoomForm,UserForm
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai


def home(request):
    data = Notes.objects.all()

    context = {'data':data}
    return render(request,'main/home.html',context)

def home_rooms(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
    Q(name__icontains=q)|
    Q(description__icontains=q))

    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))


    context = {'rooms':rooms, 'topics':topics, 'room_count': room_count, 'room_messages':room_messages}
    return render(request,'main/room.html',context)


def room_page(request,pk):

    room = Room.objects.get(id=pk)

    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room_page', pk = room.id)

    context = {'room':room, 'room_messages':room_messages, 'participants':participants}
    return render(request,'main/room_page.html',context)

def userProfile(request,pk):

    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()

    context = {'user': user,'rooms':rooms, 'room_messages':room_messages,'topics':topics}
    return render(request,'main/profile.html',context)


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'main/update-user.html', {'form': form})


@login_required(login_url='/login')
def createRoom(request):

    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('rooms')
    context = {'form':form,'topics': topics}
    return render(request, 'main/room_form.html',context)

@login_required(login_url='/login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse("Your not allowes here!!")

    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('rooms')

    context = {'form':form,'topics': topics, 'room': room}
    return render(request, 'main/room_form.html', context)

@login_required(login_url='/login')
def deleteRoom(request,pk):

    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Your not allowes here ")

    if request.method == "POST":
        room.delete()
        return redirect('rooms')

    return render(request, 'main/delete.html',{'obj':room})


@login_required(login_url='/login')
def deleteMessage(request,pk):

    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("Your not allowes here ")

    if request.method == "POST":
        message.delete()
        return redirect('rooms')

    return render(request, 'main/delete.html',{'obj':message})


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'main/topics.html', {'topics': topics})


def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'main/activity.html', {'room_messages': room_messages})








# for login and register page 


def registerPage(request):
    page = "register"
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')
        else:
            messages.error(request, 'An error occured during registration!')

    context = {'form': form}
    return render(request, 'base/login.html',context)





def login_reg(request):
    page = 'login'
   
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             messages.error(request, 'Username or password is wrong')
    context = {'page':page}
    return render(request, 'base/login.html',context)

def log_out(request):

    logout(request)
    return redirect('home')

    


# note shareing views here started
@login_required(login_url='/login')
def upload_notes(request):
    error=""
    if request.method=='POST':
        b = request.POST.get('branch')
        s = request.POST.get('subject')
        n = request.FILES.get('notesfile')
        f = request.POST.get('filetype')
        d = request.POST.get('description')
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,
                                 filetype=f,description=d,status='pending')
            error="no"
        except:
            error="yes"
    context = {}
    return render(request,'note/upload_note.html',context)

def my_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user=user)

    context = {'notes':notes}
    return render(request, 'note/my_notes.html',context)




def delete_mynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('my_notes')



# for chatgpt views

def chat(request):
    chats = Chat.objects.all()
    return render(request, 'chat/chat.html', {
        'chats': chats,
    })

@csrf_exempt
def Ajax(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': # Check if request is Ajax

        text = request.POST.get('text')
        print(text)

        openai.api_key = "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" # Here you have to add your api key.
        res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{text}"}
        ]
        )

        response = res.choices[0].message["content"]
        print(response)

        chat = Chat.objects.create(
            text = text,
            gpt = response
        )

        return JsonResponse({'data': response,})
    return JsonResponse({})