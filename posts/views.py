from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm


# Create your views here.

# 함수형 뷰
# def index(request):
#     return redirect('post-list')


# 제네릭 뷰
class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'  # 리다이렉션 할 url 패턴의 이름


# 함수형 뷰
# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6)
#     curr_page_number = request.GET.get('page')  # GET 방식으로 전달
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'posts/post_list.html', {'page': page})


# 제네릭 뷰
class PostListView(ListView):
    model = Post  # 사용할 모델
    # template_name = 'posts/post_list.html'  # 렌더링 할 템플릿. 기본값 '{모델명}_list.html'과 동일한 파일명을 사용하고 있어서 생략 가능
    # context_object_name = 'posts'  # 조회한 데이터를 컨텍스트로 넘겨줄 데이터 이름. post_list.html에서 기본값 '{모델명}_list' 또는 'object_list'와 동일한 변수명을 사용하고 있으면 생략 가능
    ordering = ['-dt_created']  # 가장 최근 게시글이 맨 위로 올라오도록 정렬(내림차순)
    paginate_by = 6  # 페이지네이션, 몇개 단위로 페이지를 나눌 건지
    # page_kwarg = 'page'  # 현재 페이지를 쿼리스트링의 어떤 값으로 조회하는지를 알려준다. 기본값 page와 동일하기 때문에 생략 가능


# 함수형 뷰
# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     context = {"post": post}
#     return render(request, 'posts/post_detail.html', context)


# 제네릭 뷰
class PostDetailView(DetailView):
    model = Post  # 사용할 모델
    # template_name = 'posts/post_detail.html'  # 렌더링 할 템플릿. 기본값 '{모델명}_detail.html'과 동일한 파일명을 사용하고 있어서 생략 가능
    # pk_url_kwarg = 'post_id'  # urls.py에서 전달된 id 값. urls.py에서 기본값 'pk'를 사용하면 생략 가능
    # context_object_name = 'post'  # 조회한 데이터를 컨텍스트로 넘겨줄 데이터 이름. 기본값 '{모델명}'을 사용하고 있어서 생략 가능


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
    model = Post  # 사용할 모델
    form_class = PostForm  # 유저의 입력을 받기 위한 폼.
    # template_name = 'posts/post_form.html'  # 렌더링 할 템플릿. 기본값 '{모델명}_form.html'과 동일한 파일명을 사용하고 있어서 생략 가능

    # 글 작성이 되면 detail 페이지로 이동
    def get_success_url(self):
        # reverse: url 네임으로부터 거슬러 올라가서 url을 찾는다.
        # kwargs : 사전형으로 키워드를 이용해서 값을 전달할 때 사용하는 인자
        # self.object.id : 현재 새로 생성된 데이터 객체에 접근할 수 있다.
        # return reverse('post-detail', kwargs={'post_id': self.object.id})
        return reverse('post-detail', kwargs={'pk': self.object.id})  # 'post_id' 대신 기본값 'pk' 사용


# 함수형 뷰
# def post_update(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         # 작성된 데이터(request.POST)와 폼(PostForm)을 바인딩 하는데
#         # 기존에 작성되었던 Post 모델 인스턴스(instance=post)와 수정된 데이터를 갖는 폼을 만든다. -> 수정기능의 핵심
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post_id)
#     else:
#         post_form = PostForm(instance=post)  # 기존 모델의 데이터를 가져와서 채운 상태의 폼을 제공
#     return render(request, 'posts/post_form.html', {'form': post_form})


# 제네릭 뷰
class PostUpdateView(UpdateView):
    model = Post  # 사용할 모델
    form_class = PostForm  # 유저의 입력을 받기 위한 폼
    # template_name = 'posts/post_form.html'  # 렌더링 할 템플릿. 기본값 '{모델명}_form.html'과 동일한 파일명을 사용하고 있어서 생략 가능
    # pk_url_kwarg = 'post_id'  # urls.py에서 전달된 id 값
    # pk_url_kwarg = 'pk'  # 'post_id' 대신 기본값 'pk' 사용. urls.py에서 기본값 'pk'를 사용하면 생략 가능

    # 수정된 데이터의 유효성 검증이 성공하면 이동할 url
    def get_success_url(self):
        # return reverse('post-detail', kwargs={'post_id': self.object.id})
        return reverse('post-detail', kwargs={'pk': self.object.id})  # 'post_id' 대신 기본값 'pk' 사용


# 함수형 뷰
# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post-list')
#     else:
#         return render(request, 'posts/post_confirm_delete.html', {'post': post})


class PostDeleteView(DeleteView):
    model = Post  # 사용할 모델
    # template_name = 'posts/post_confirm_delete.html'  # 렌더링 할 템플릿. 기본값 '{모델명}_confirm_delete.html'과 동일한 파일명을 사용하고 있어서 생략 가능
    # pk_url_kwarg = 'post_id'  # urls.py에서 전달된 id 값. 이 값으로 데이터를 조회한 다음에 만약에 id 값에 해당하는 데이터가 없으면 404 에러를 내는 과정까지 django가 내부적으로 처리한다.
    # pk_url_kwarg = 'pk'  # 'post_id' 대신 기본값 'pk' 사용. urls.py에서 기본값 'pk'를 사용하면 생략 가능
    # context_object_name = 'post'  # 조회한 데이터를 컨텍스트로 넘겨줄 데이터 이름. 기본값 '{모델명}'을 사용하고 있어서 생략 가능

    # 삭제를 하고 난 후 이동할 url
    def get_success_url(self):
        return reverse('post-list')
