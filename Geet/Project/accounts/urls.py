from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.registration, name="signup"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('upload/', views.upload, name="upload"),
    path('startlistening/<int:id>/', views.player, name="player"),    path('listenlater/', views.watchlater, name="watchlater"),
    path('startlistening/', views.startlistening, name="startlistening"),
    path('channel/',views.channel,name="channel"),
    path('', views.index, name="home"),
    path('r/<str:channel>', views.channel, name='channel'),
    path('listenlater/', views.watchlater, name="watchlater"),
    path('history/',views.history ,name='history'),

]

