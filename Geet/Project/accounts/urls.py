from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.registration, name="signup"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('upload/', views.upload, name="upload"),
    path('startlistening/<int:id>/', views.player, name="player"),    
    path('startlistening/', views.startlistening, name="startlistening"),
    path('channel/',views.channel,name="channel"),
    path('', views.index, name="home"),
    path('community/', views.community, name="community"),
  
    path('listenlater/', views.listenlater , name="listenlater"),
    path('history/',views.history ,name='history'),
    path('search/',views.search ,name='search'),

]

