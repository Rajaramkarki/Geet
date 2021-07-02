from django.conf.urls import url
from .import views


app_name='community'

urlpatterns=[
    url('post/',views.Post_list,name='post'),
    url('<int:year>/<int:month>/<int:day>/<slug:post>',views.show_post,name='show_post'),
]
