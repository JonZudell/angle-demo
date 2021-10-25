from .views import PostList, FilterPostList
from django.urls import path, re_path

urlpatterns = [
    path('', PostList.as_view()),
    re_path('^search/.*$', FilterPostList.as_view())
]