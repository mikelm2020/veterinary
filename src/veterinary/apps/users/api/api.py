from apps.users.api.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignupSerializer,
)
from apps.users.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"])
    def login(self, request):
        """
        User sing in
        """
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {"user": UserModelSerializer(user).data, "access_token": token}
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def signup(self, request):
        """
        User signup
        """
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
