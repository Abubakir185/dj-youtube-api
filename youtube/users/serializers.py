from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import User, Channel, Comment, Video, CommentLike, VideoLike

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'full_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def validate(self, attrs):
        ism_familiya = attrs['full_name']
        if ism_familiya:
            for i in ism_familiya:
                if i.isdigit():
                    raise ValidationError("Ism familiyada raqam bo'lishi mumkinmas")
        return attrs



class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = ['user', 'bio', 'name']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'video', 'text']

    

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_cover', 'video_url', 'video_file', 'channel', 'title', 'description', ]


class CommentLikeSerializer(ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['user', 'comment', 'status']


class VideoLikeSerializer(ModelSerializer):
    class Meta:
        model = VideoLike
        fields = ['user', 'video', 'status']
