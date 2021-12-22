from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    )
from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('user/<username>/',UserPostListView.as_view(), name = 'user_posts'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('post/new/', PostCreateView.as_view(), name = 'new_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    
    path('', PostListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
