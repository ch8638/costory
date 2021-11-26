from django.urls import path
from . import views


# path의 name 인자는 view와 template에 URL을 직접 입력하지 않고 참조 형식으로 작성하도록 하여 하드코딩을 피할 수 있다.
# <int:post_id> : views.post_detail에 int형 변수 post_id를 넘겨준다.
urlpatterns = [
    # 함수형 뷰
    # path('', views.index, name='index'),
    # path('posts/', views.post_list, name='post-list'),
    # path('posts/new/', views.post_create, name='post-create'),
    # path('posts/<int:post_id>', views.post_detail, name='post-detail'),
    # path('posts/<int:post_id>/edit', views.post_update, name='post-update'),
    # path('posts/<int:post_id>/delete', views.post_delete, name='post-delete'),
    # 제네릭 뷰
    path('', views.IndexRedirectView.as_view(), name='index'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    # path('posts/<int:post_id>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    # path('posts/<int:post_id>/edit', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/edit', views.PostUpdateView.as_view(), name='post-update'),
    # path('posts/<int:post_id>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
]
