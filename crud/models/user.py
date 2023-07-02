from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator


class SoilUser(AbstractUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        db_table = "users"
        
        verbose_name_plural = "Usuários"
        verbose_name = "Usuário"
        ordering = ["username", "id"]
        indexes = [
            models.Index(fields=["username"]),
            models.Index(fields=["username"], name="user_name_idx"),
        ]

    USER_TYPE_CHOICES = (("USER", "USER"), ("SUDO", "SUDO"), ("DEALER", "DEALER"))
    login = models.CharField(max_length=10, blank=True, null=True)
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, blank=False, null=False
    )
    user_id = models.CharField(max_length=100, unique=True, blank=False)

    REQUIRED_FIELDS = ["password", "user_type"]

    def __str__(self):
        return str(self.username)
