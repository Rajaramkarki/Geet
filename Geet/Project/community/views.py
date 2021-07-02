from django.shortcuts import get_object_or_404, render
from .models import Postmodel

# Create your views here.


def Post_list(request):
    posts=Postmodel.published.all()
    return render(request,'community/post.html',{'posts':posts})


def show_post(request,year,month,day,post):
    post=get_object_or_404(Postmodel,slug=post,status='Published',
                            published_year=year,published_month=month,published_day=day) 
    return render(request,'post_detail.html',{'post':post})                          