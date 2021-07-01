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
    

def watchlater(request):
    if request.method== "POST":
        user=request.user
        video_id=request.POST['video_id']
        
        
        watch= Listenlater.objects.filter(user=user)

        for i in watch:
            if video_id== i.video_id:
                message= "Your song is already added"
                break
        else:
            watchlater = Listenlater(user=user, video_id = video_id)
            watchlater.save()
            message="Your song is successfuly added"
        
        song = Song.objects.all()
        return render(request, 'accounts/startlistening.html', { 'song':song,  "message": message})
    
    wl=Listenlater.objects.filter(user=request.user)
    ids=[]
    for i in wl:
        ids.append(i.video_id)
        
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

def songpost(request, id):
    song=Song.objects.filter(sing_id=id).first()
    return render( request ,'accounts/songpost.html',{'song':song}  )

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
        


