from django.urls import path
from .views import BlogView, ArticeDetailView, AddPostView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:pk>', ArticeDetailView.as_view(), name='article-detail'),
    


]