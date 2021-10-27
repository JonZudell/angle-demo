from .views import PostList
from django.urls import path, re_path

urlpatterns = [
    path('', PostList.as_view())
]