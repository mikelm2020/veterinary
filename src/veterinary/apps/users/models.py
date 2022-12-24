from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

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

    username = models.CharField(max_length=10, unique=True)
    name = models.CharField("Nombre", max_length=50, blank=True, null=True)
    last_name = models.CharField("Apellidos", max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    degree = models.CharField(
        "Grado Escolar", max_length=1, blank=True, null=True, choices=DEGREE_CHOICES
    )
    phone = models.CharField("Teléfono", max_length=12, blank=True, null=True)
    professional_license = models.CharField(
        "Cédula Profesional", max_length=30, default="Ninguna"
    )
    user_type = models.CharField(
        "Tipo de Usuario", max_length=1, choices=USER_TYPE_CHOICES
    )
    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "last_name"]

    def __str__(self):
        return f"{self.name} {self.last_name}"
