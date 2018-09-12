from django.shortcuts import render
from django.shortcuts import redirect
from .models import Userinfor
from .models import Post
from .forms import PostForm

def home(request):
    posts1 = Post.objects.filter(id = 1)
    posts2 = Post.objects.filter(id = 2)
    posts3 = Post.objects.filter(id = 3)
    prof = Userinfor.objects.filter(id = 2)

    d = {
        'posts1': posts1,
        'posts2': posts2,
        'posts3': posts3,
        'prof': prof,
    }
    return render(request, 'main/home.html', d)

def tweet(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.userids = request.user
            post.save()
            return redirect(home)

    else:
        form = PostForm()

    return render(request, 'main/form.html', {'form': form})
