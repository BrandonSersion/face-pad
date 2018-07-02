from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import User, Content, Rate, Comment, Friend
from .permissions import IsUser, IsUserOrFriend
from .serializers import CreateUserSerializer, UserSerializer, ContentSerializer, RateSerializer, CommentSerializer, FriendSerializer
from .mixins import MixedPermissionModelMixin


class UserViewSet(MixedPermissionModelMixin,
                  viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, and retrieves user accounts.
    """

    # On POST or PUT request uses special serializer that encrypts password
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return CreateUserSerializer
        return UserSerializer

    queryset = User.objects.all()
    permission_classes_by_action = {
        'create': [AllowAny],
        'update': [IsUser],
        'delete': [IsAdminUser],
        'list': [IsAdminUser],
        'retrieve': [IsUserOrFriend],  # TODO fix bug where admins can't retrieve
    }


class ContentViewSet(MixedPermissionModelMixin,
                     viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, and retrieves contents.
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'update': [IsAdminUser],
        'delete': [IsAdminUser],
        'list': [IsAdminUser],
        'retrieve': [IsUserOrFriend],
    }


class RateViewSet(MixedPermissionModelMixin,
                  viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, and retrieves rates.
    """
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes_by_action = {
        'create': [IsUserOrFriend],
        'update': [IsAdminUser],
        'delete': [IsAdminUser],
        'list': [IsAdminUser],
        'retrieve': [IsUserOrFriend],
    }


class CommentViewSet(MixedPermissionModelMixin,
                     viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, and retrieves comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes_by_action = {
        'create': [IsUserOrFriend],
        'update': [IsAdminUser],
        'delete': [IsAdminUser],
        'list': [IsAdminUser],
        'retrieve': [IsUserOrFriend],
    }


class FriendViewSet(viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, and retrieves friend links.
    """
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = (IsUser,)