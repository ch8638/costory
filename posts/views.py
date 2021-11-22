from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    return redirect('post-list')


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    curr_page_number = request.GET.get('page')  # GET 방식으로 전달
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number)
    return render(request, 'posts/post_list.html', {'page': page})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)

# 함수형 뷰
# def post_create(request):
#     if request.method == 'POST':  # http 전달 방식이 POST 이면
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():  # 유효성 검사
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)
#     else:  # http 전달 방식이 GET 이면
#         post_form = PostForm()  # 빈 폼 불러오기
#     return render(request, 'posts/post_form.html', {'form': post_form})


# 클래스형 뷰
# class PostCreateView(View):
#     def get(self, request):  # GET 방식
#         post_form = PostForm()  # 빈 폼 불러오기
#         return render(request, 'posts/post_form.html', {'form': post_form})
#
#     def post(self, request):  # POST 방식
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():  # 유효성 검사
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)
#         return render(request, 'posts/post_form.html', {'form': post_form})


# 제네릭 뷰
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})
        # reverse: url 네임으로부터 거슬러 올라가서 url을 찾는다.
        # kwargs : 사전형으로 키워드를 이용해서 값을 전달할 때 사용하는 인자


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



