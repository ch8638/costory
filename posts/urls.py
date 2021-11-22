from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post-list'),  # path의 name 인자는 view와 template에 URL을 직접 입력하지 않고 참조 형식으로 작성하도록 하여 하드코딩을 피할 수 있다.
    # path('posts/new/', views.post_create, name='post-create'),  # 함수형 view
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),  # 클래스형 view
    path('posts/<int:post_id>', views.post_detail, name='post-detail'),  # <int:post_id> : views.post_detail에 int형 변수 post_id를 넘겨준다.
    path('posts/<int:post_id>/edit', views.post_update, name='post-update'),
    path('posts/<int:post_id>/delete', views.post_delete, name='post-delete'),
]
