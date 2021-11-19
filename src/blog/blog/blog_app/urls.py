from django.urls import path
from blog.blog_app.views import home, about, PostListView, PostDetailView, PostCreateView, PostUpdateView, \
    PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='blog-about'),
]
