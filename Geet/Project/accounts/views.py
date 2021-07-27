from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Case, When

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    song = Song.objects.all()
    return render(request, 'index.html', {'song':song})

def listenlater(request):
    
    if request.method== "POST":
        user=request.user
        later_id=request.POST['later_id']
        
        
        listen= Listenlater.objects.filter(user=user)

        for i in listen:

            if later_id== i.later_id:
                message= "Your Song is already added"
                break
        else:
            watchlater = Listenlater(user=user, later_id = later_id)
            watchlater.save()
            message="Your Song is successfuly added"
        
        song = Song.objects.filter(song_id=later_id).first()
        return render(request, f"accounts/player.html", {'song': song, "message": message})
    
    wl=Listenlater.objects.filter(user=request.user).order_by('-added_at')
    ids=[]
    for i in wl:
        ids.append(i.later_id)
        
    preserved = Case(*[When(pk=pk, then= pos) for pos, pk in enumerate(ids)])
    song= Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "accounts/listenlater.html", {'song': song})

def upload(request):
        if request.method=="POST":
            song_name=request.POST["Song name"]
            singer_name=request.POST["Singer"]
            genre = request.POST["Genre"]
            songs = request.FILES["InputFile"]
            image= request.FILES["InputImage"]
            song_model = Song(song_name=song_name, singer_name=singer_name, song_genre=genre, image=image, song=songs)
            song_model.save()
        return render(request, 'accounts/upload.html')

def startlistening(request):
    song = Song.objects.all()
    return render(request, 'accounts/startlistening.html',{'song':song})

def player(request, id):
    song = Song.objects.filter(song_id = id).first()
    return render(request, 'accounts/player.html',{'song':song})

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUser()
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def channel(request, channel):
        

    return render(request, "accounts/channel.html")

def history(request):
    if request.method== "POST":
        user=request.user
        music_id=request.POST['music_id']
        history = History(user=user, music_id = music_id)
        history.save()
        
        return redirect(f"/accounts/startlistening/{music_id}")
    
    history=History.objects.filter(user=request.user).order_by('-done_at')
    H=[]
    for i in history:
        H.append(i.music_id)
    
    preserved = Case(*[When(pk=pk, then= pos) for pos, pk in enumerate(H)])
    song= Song.objects.filter(song_id__in=H).order_by(preserved)

    return render(request, 'accounts/history.html',{'song':song})


