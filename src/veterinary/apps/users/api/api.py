from apps.users.api.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignupSerializer,
)
from apps.users.models import User
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework import status, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    permission_classes = [AllowAny]

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
