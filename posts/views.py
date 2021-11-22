from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return redirect('post-list')


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    context = {"posts": posts}
    return render(request, 'posts/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':  # http 전달 방식이 POST 이면
        post_form = PostForm(request.POST)
        if post_form.is_valid():  # 유효성 검사
            new_post = post_form.save()
            return redirect('post-detail', post_id=new_post.id)
    else:  # http 전달 방식이 GET 이면
        post_form = PostForm()  # 빈 폼 불러오기
    return render(request, 'posts/post_form.html', {'form': post_form})


def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # 작성된 데이터(request.POST)와 폼(PostForm)을 바인딩 하는데
        # 기존에 작성되었던 Post 모델 인스턴스(instance=post)와 수정된 데이터를 갖는 폼을 만든다. -> 수정기능의 핵심
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post_id=post_id)
    else:
        post_form = PostForm(instance=post)  # 기존 모델의 데이터를 가져와서 채운 상태의 폼을 제공
    return render(request, 'posts/post_form.html', {'form': post_form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'posts/post_confirm_delete.html', {'post': post})



