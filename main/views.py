from django.shortcuts import render
from .models import Userinfor
from .models import Post

def home(request):
    posts1 = Post.objects.filter(id = 1)
    posts2 = Post.objects.filter(id = 2)
    posts3 = Post.objects.filter(id = 3)
    prof = Userinfor.objects.filter(id = 1)

    d = {
        'posts1': posts1,
        'posts2': posts2,
        'posts3': posts3,
        'prof': prof,
    }
    return render(request, 'main/home.html', d)
