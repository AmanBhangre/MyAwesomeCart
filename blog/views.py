from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    posts = Blogpost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def blogpost(request, postid):
    post = Blogpost.objects.get(post_id=postid)
    
    return render(request, 'blog/blogpost.html', {'post': post})