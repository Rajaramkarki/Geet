from django.core import paginator
from django.shortcuts import get_object_or_404, render
from .models import Postmodel
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.

def Post_list(request):
    object_list=Postmodel.published.all().order_by('-publish')
    paginator=Paginator(object_list,4)
    page=request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'community/post.html',{'page':page,'posts':posts})


def show_post(request,year,month,day,post):
    post=get_object_or_404(Postmodel,slug=post,
                            publish__year=year,publish__month=month,publish__day=day) 
    return render(request,'community/post_detail.html',{'post':post})                          