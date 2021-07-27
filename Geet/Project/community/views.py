from django.core import paginator
from django.forms.forms import Form
from django.shortcuts import get_object_or_404, render
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,UpdateView,DeleteView
from accounts.models import Song

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


def post_detail(request,pk):
    post=get_object_or_404(Postmodel,id=pk) 
                     
    comments=post.comments.filter(active=True)         
    new_comment=None

    if request.method=='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            new_comment=comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,'community/post_detail.html',{'post':post,'comments':comments,
                                                        'new_comment':new_comment,'comment_form':comment_form})   


class Postcreateview(LoginRequiredMixin,CreateView):
    model=Postmodel
    fields=['title','slug','body','status']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def sharing(request, id):
    model=Postmodel
    fields=['title','slug','body','status']
    song = Song.objects.filter(song_id = id).first()
    return render(request, 'community/postmodel_form.html',{'song':song})

class Postupdateview(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    model=Postmodel
    fields=['title','slug','body','status']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model=Postmodel
    success_url='/community/post'
 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def post_share(request,post_id):
    post=get_object_or_404(Postmodel,id=post_id)
    sent = False
    if request.method== 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            #....it send email
            post_url= request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail=(subject,message,'adityakhadka907@gmai.com', cd['to'])
            sent = True
    else:
        form=EmailForm()
    return render (request,'community/post_share.html',{'post':post,'form':form,'sent':sent})        
