from django.shortcuts import HttpResponse
from rest_framework import viewsets
# from rest_framework import generics
from .models import User, Channel, Comment, Video, VideoLike, CommentLike
from .serializers import VideoSerializer, CommentSerializer, ChannelSerializer, UserSerializer, VideoLikeSerializer, CommentLikeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

# class ChannelAPIView(generics.ListCreateAPIView):
#     queryset = Channel.objects.all()
#     serializer_class = ChannelSerializer

# class ChannelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Channel.objects.all()
#     serializer_class = ChannelSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# class CommentAPIView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

# class VideoAPIView(generics.ListCreateAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer

# class VideoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer

class VideoLikeViewSet(viewsets.ModelViewSet):
    queryset = VideoLike.objects.all()
    serializer_class = VideoLikeSerializer

# class VideoLikeAPIView(generics.ListCreateAPIView):
#     queryset = VideoLike.objects.all()
#     serializer_class = VideoLikeSerializer

# class VideoLikeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = VideoLike.objects.all()
#     serializer_class = VideoLikeSerializer

class CommentLikeViewSet(viewsets.ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer

# class CommentLikeAPIView(generics.ListCreateAPIView):
#     queryset = CommentLike.objects.all()
#     serializer_class = CommentLikeSerializer

# class CommentLikeDetailkAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CommentLike.objects.all()
#     serializer_class = CommentLikeSerializer


def home_page(request):
    return HttpResponse("Hi")