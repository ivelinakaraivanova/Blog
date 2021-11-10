from django.urls import path
from blog.blog_app.views import home, about

urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about'),
]