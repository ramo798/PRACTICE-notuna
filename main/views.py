from django.shortcuts import render
from django.shortcuts import redirect
from .models import Userinfor
from .models import Post
from .forms import PostForm
import random

def home(request):
    #ログイン中のユーザーのプロフを表示
    prof = Userinfor.objects.filter(userid = request.user)

    #ログイン中のユーザーのツイートを表示
    posts = Post.objects.filter(userids = request.user)

    #一覧の名前と画像用の読み込み
    itiran = Userinfor.objects.all()

    d = {
        'posts': posts,
        'prof': prof,
        'itiran': itiran,
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
