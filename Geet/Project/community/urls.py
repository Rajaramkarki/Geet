from django.urls import path
from .import views


app_name='community'

urlpatterns=[
    
    path('post/', views.Post_list, name='post'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.show_post, name='show_post'),
]
