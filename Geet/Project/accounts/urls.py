from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.registration, name="signup"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="password_reset"), #submit email in form
    path('password_reset/done/',auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_done"),  # link sent to email to reset pw
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),name="password_reset_confirm"),  #present a form to enter new pw
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),  # pw succesfully change msg
    path('upload/', views.upload, name="upload"),
    path('startlistening/<int:id>/', views.player, name="player"),    
    path('startlistening/', views.startlistening, name="startlistening"),
    path('channel/',views.channel,name="channel"),
    path('', views.index, name="home"),
    path('r/<str:channel>', views.channel, name='channel'),
    path('listenlater/', views.listenlater , name="listenlater"),
    path('history/',views.history ,name='history'),

]

