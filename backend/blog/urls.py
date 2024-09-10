from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListCreateView.as_view(), name='post-list'),
    path('<str:pk>/', views.PostDetailView.as_view(), name='post-details'),
    path('<str:pk>/update/', views.PostUpdateView.as_view(), name='post-Update'),
    path('<str:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
]
