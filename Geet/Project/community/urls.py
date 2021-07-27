from django.urls import path
from .import views


app_name='community'

urlpatterns=[
    
    path('post/', views.Post_list, name='post'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',views.post_share, name='post_share'),
    path('post/create/',views.Postcreateview.as_view(),name='create-post'),
    path('post/create/<int:id>',views.sharing,name='create-post'),
    path('post/<int:pk>/update/',views.Postupdateview.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
