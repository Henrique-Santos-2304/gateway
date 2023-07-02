from django.db import models
from crud.models import Pivots, SoilUser
from crud.utils.set_foreign_null import get_sentinel_user


class States(models.Model):
    class Meta:
        db_table = "states"
        verbose_name_plural = "Estados dos pivôs"
        verbose_name = "Estados do pivô"
        ordering = ["pivot_id", "id"]
        indexes = [
            models.Index(fields=["state_id", "pivot_id"]),
            models.Index(fields=["state_id"], name="state_name_idx"),
        ]

    DIRECTION_OPTIONS = (
        ("CLOCKWISE", "CLOCKWISE"),
        ("ANTI_CLOCKWISE", "ANTI_CLOCKWISE"),
    )
    state_id = models.CharField(max_length=90)
    pivot_id = models.ForeignKey(
        Pivots, on_delete=models.CASCADE, related_name="pivot_of_state"
    )
    author = models.ForeignKey(
        Pivots, on_delete=models.SET(get_sentinel_user), related_name="author_of_state"
    )
    power = models.BooleanField()
    water = models.BooleanField()
    connection = models.BooleanField()
    pressure = models.BooleanField()
    start_angle = models.IntegerField()

    direction = models.CharField(max_length=20, choices=DIRECTION_OPTIONS)
    timestamp = models.DateTimeField()

    def __str__(self):
        message = self.pivot_id or "Não encontrado"
        return f"Estados do Pivô {message}".upper()
