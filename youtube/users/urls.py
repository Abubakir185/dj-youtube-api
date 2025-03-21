# from users.views import VideoDetailAPIView, VideoAPIView, CommentDetailAPIView, CommentAPIView, ChannelDetailAPIView, ChannelAPIView, UserDetailAPIView, UserAPIView, VideoLikeAPIView, VideoLikeDetailAPIView, CommentLikeAPIView, CommentLikeDetailkAPIView
from .views import CommentLikeViewSet, VideoLikeViewSet, VideoViewSet, CommentViewSet, ChannelViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
# from users import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)  # Avtomatik CRUD marshrutlar
router.register(r'comments', CommentViewSet)
router.register(r'channels', ChannelViewSet)
router.register(r'Video', VideoViewSet)
router.register(r'videolikes', VideoLikeViewSet)
router.register(r'commentlikes', CommentLikeViewSet)



urlpatterns = [
    path('', include(router.urls)),

    # path("videos/", VideoAPIView.as_view(), name="videos"),
    # path("videos/<int:pk>/", VideoDetailAPIView.as_view()),

    # path("comments/", CommentAPIView.as_view(), name="comments"),
    # path("comments/<int:pk>/", CommentDetailAPIView.as_view()),

    # path("channels/", ChannelAPIView.as_view(), name="channels"),
    # path("channels/<int:pk>/", ChannelDetailAPIView.as_view()),

    # path("users/", UserAPIView.as_view(), name="videos"),
    # path("users/<int:pk>/", UserDetailAPIView.as_view()),

    # path("videolike/", VideoLikeAPIView.as_view(), name="videolikes"),
    # path("videolike/<int:pk>/", VideoLikeDetailAPIView.as_view()),

    # path("commentlike/", CommentLikeAPIView.as_view(), name="commentlike"),
    # path("commentlike/<int:pk>/", CommentLikeDetailkAPIView.as_view())
]   
