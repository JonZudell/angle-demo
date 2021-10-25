from .models import Post
from .serializers import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
#from django_filters import rest_framework as filters

#class PostFilter(filters.FilterSet):
#    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
#    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
#    keyword = filters.CharFilter(field_name="keyword", lookup_expr='icontains')
#
#    class Meta:
#        model = Post

class PostList(APIView):
    """
    Creates a post.
    """
    #def get(self, request, format=None):
    #    posts = Post.objects.all()
    #    serializer = Post Serializer(posts, many=True)
    #    return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilterPostList(generics.ListAPIView):

#    queryset = Product.objects.all()
    serializer_class = PostSerializer
#    filter_backends = (filters.DjangoFilterBackend,)
#    filterset_class = PostFilter
    def get_queryset(self):
        """
        This view filters by keyword and prices
        """
        queryset = Post.objects.all()

        keyword = self.request.query_params.get("keyword")
        if keyword is not None:
            queryset = queryset.filter(name__contains=keyword)

        min_price = self.request.query_params.get("min_price")
        if min_price is not None:
            queryset = queryset.exclude(price__lt=min_price)

        max_price = self.request.query_params.get("max_price")
        if max_price is not None:
            queryset = queryset.exclude(price__gt=max_price)
            
        return queryset