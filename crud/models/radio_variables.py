from django.db import models
from crud.models import Pivots, SoilUser
from crud.utils.set_foreign_null import get_sentinel_user


class RadioVariables(models.Model):
    class Meta:
        db_table = "radio_variables"
        verbose_name_plural = "Sinais dos Radios"
        verbose_name = "Sinais do Radio"
        ordering = ["pivot_id"]
        indexes = [
            models.Index(fields=["pivot_id"]),
            models.Index(fields=["pivot_id"], name="radio_variable_idx"),
        ]

    radio_variable_id = models.CharField(max_length=90, blank=True, null=True)
    pivot_id = models.ForeignKey(
        Pivots, on_delete=models.CASCADE, related_name="pivot_of_radio_variable"
    )

    father = models.TextField(blank=True, null=True)
    rssi = models.FloatField(blank=True, null=True)
    noise = models.FloatField(blank=True, null=True)

    timestamp = models.DateTimeField()

    def __str__(self):
        message = self.pivot_id or "Não encontrado"

        return str(f"Rssi, Father e Noise do pivô {message}").upper()
