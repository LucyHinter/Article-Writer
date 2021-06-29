from django.db.models.fields import CharField
from django.shortcuts import render
from .models import Posts
# Create your views here.

def home(request):
    return render(request, 'editor/home.html',{
        "posts": Posts.objects.all()
    })

def post(request, post_id):
    post = Posts.objects.get(pk=post_id)
    return render(request, "editor/viewpage.html",{
        "post":post
    })




