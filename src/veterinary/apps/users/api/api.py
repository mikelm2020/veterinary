from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.users.api.serializers import UserLoginSerializer, UserModelSerializer
from apps.users.models import User

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    @action(detail=False, methods=["post"])
    def login(self, request):
        """
        user sing in
        """
        import pdb; pdb.set_trace()
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data={
            'user': UserModelSerializer(user),
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
