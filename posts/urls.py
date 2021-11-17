from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('posts/', views.post_list, name='post-list'),
    # path('posts/new', views.post_create),
    path('posts/<int:post_id>', views.post_detail, name='post-detail'),  # views.post_detail에 int형 변수 post_id를 넘겨준다.
    # path('posts/<int:post_id>/edit', views.post_update),
    # path('posts/<int:post_id>/delete', views.post_delete),
]