from rest_framework import serializers
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token
from apps.users.models import User


class UserLoginSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=10)
        password = serializers.CharField(min_length=8, max_length=64)

        # def validate_username(self, value):
        #     if len(value) > 10:
        #         raise serializers.ValidationError("El username debe tener maximo 10 caracteres")
        #     return value

        # def validate_password(self, value):
        #     if len(value) < 8:
        #         raise serializers.ValidationError("El password debe tener como minimo 8 caracteres")
        #     if len(value) > 64:
        #         raise serializers.ValidationError("El password debe tener como máximo 64 caracteres")
        #     return value

        def validate(self, data):
            user = authenticate(username=data["username"], password=data["password"])
            if not user:
                raise serializers.ValidationError("Las credenciales no son vaĺidas")

            self.context["user"] = user
            return data

        def create(self, data):
            token, created = Token.objects.get_or_create(user=self.context["user"])
            return self.context["user"], token.key


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "name",
            "last_name",
            "degree",
            "phone",
            "professional_license",
            "user_type",
        )
