from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required

from .forms import *

def home(request):
    return render(request, 'base.html')

def post(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(
        request,
        'pages/post.html',
        context
    )


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    context = {
        'post': post,
        'user': user
    }
    return render(request, 'pages/post_detail.html', context)
    
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(to='post')
    else: 
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)

def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect(to='post')