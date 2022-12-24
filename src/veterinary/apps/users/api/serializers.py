from apps.users.models import User
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


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


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Las credenciales no son vaĺidas")

        self.context["user"] = user
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context["user"], token.key


class UserSignupSerializer(serializers.Serializer):
    

    DEGREE_CHOICES = (
        ("S", "Superior"),
        ("M", "Media"),
        ("B", "Básica"),
    )

    USER_TYPE_CHOICES = (
        ("G", "Gerente"),
        ("V", "Veterinario(a)"),
        ("R", "Recepcionista"),
        ("A", "Asistente"),
    )

    username = serializers.CharField(
        min_length=4,
        max_length=10,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=50)
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirm = serializers.CharField(min_length=8, max_length=64)
    degree = serializers.ChoiceField(choices=DEGREE_CHOICES, required=False)
    phone_regex = RegexValidator(regex=r"\d{10,12}$")
    phone = serializers.CharField(validators=[phone_regex], required=False)
    professional_license = serializers.CharField(
        max_length=30, required=False
    )
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)

    def validate(self, data):
        password_var = data["password"]
        password_confirm_var = data["password_confirm"]
        if password_var != password_confirm_var:
            raise serializers.ValidationError(
                {"password": "Las contraseñas no coinciden"}
            )
        password_validation.validate_password(password_var)

        # degree_var = data["degree"]
        # professional_license_var = data["professional_license"]
        # if degree_var == "S" and professional_license_var == "Ninguna":
        #     raise serializers.ValidationError(
        #         {"professional_license": "Debes registrar la cédula profesional"}
        #     )

        return data

    def create(self, data):
        data.pop("password_confirm")
        user = User.objects.create_user(**data)
        return user
