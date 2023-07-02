from django.db import models
from crud.models import Pivots, Farm


class LastState(models.Model):
    class Meta:
        db_table = "last_state"
        verbose_name_plural = "Último estado"
        verbose_name = "Último estado"
        ordering = ["pivot_id"]
        indexes = [
            models.Index(fields=["pivot_id", "farm_id"]),
            models.Index(fields=["pivot_id"], name="last_state_name_idx"),
        ]

    pivot_id = models.ForeignKey(
        Pivots, on_delete=models.CASCADE, related_name="pivot_of_last_state"
    )
    farm_id = models.ForeignKey(
        Farm, on_delete=models.CASCADE, related_name="farm_of_last_state"
    )
    angle = models.IntegerField()
    state = models.CharField(max_length=60)
    timestamp = models.DateTimeField()

    def __str__(self):
        message = self.pivot_id or "Não encontrado"

        return f"ÚLTIMO ESTADO DO PIVÔ {message}".upper()
