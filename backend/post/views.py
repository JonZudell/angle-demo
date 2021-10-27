from .models import Post
from .serializers import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
import django_filters 

class PostFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    keyword = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ["name", "price", "start_date"]

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    serializer_class = PostSerializer
    filter_class = PostFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"posts" : serializer.data})

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data["posts"], many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"posts" : serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"posts" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)