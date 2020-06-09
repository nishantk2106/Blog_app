from django.urls import path
from .views import postListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserpostListView
from . import views

urlpatterns = [
    path('user/<str:username>', UserpostListView.as_view(),name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('about/', views.about,name='blog-about'),
    path('', postListView.as_view(),name='blog-home'),
]


