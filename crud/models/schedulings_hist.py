from django.db import models
from crud.models import Pivots, SoilUser
from crud.utils.set_foreign_null import get_sentinel_user


class SchedulingHistory(models.Model):
    class Meta:
        db_table = "scheduling_historys"
        verbose_name_plural = "Histórico dos agendamentos"
        verbose_name = "Histórico de agendamento"
        ordering = ["pivot_id"]
        indexes = [
            models.Index(fields=["pivot_id", "scheduling_id"]),
            models.Index(fields=["pivot_id"], name="scheduling_idx"),
        ]

    DIRECTION_OPTIONS = (
        ("CLOCKWISE", "CLOCKWISE"),
        ("ANTI_CLOCKWISE", "ANTI_CLOCKWISE"),
    )

    scheduling_id = models.CharField(max_length=90, blank=True, null=True)
    pivot_id = models.ForeignKey(
        Pivots, on_delete=models.CASCADE, related_name="pivot_of_scheduling_hist"
    )
    author = models.ForeignKey(
        SoilUser,
        on_delete=models.SET(get_sentinel_user),
        related_name="author_of_scheduling_hist",
        blank=True,
        null=True,
    )
    is_stop = models.BooleanField(blank=True, null=True)
    is_return = models.BooleanField(blank=True, null=True)
    power = models.BooleanField()
    water = models.BooleanField()
    direction = models.CharField(max_length=20, choices=DIRECTION_OPTIONS)
    start_date_of_module = models.CharField(max_length=255)
    start_angle = models.IntegerField(blank=True, null=True)
    percentimeter = models.IntegerField(blank=True, null=True)
    start_timestamp = models.DateTimeField(blank=True, null=True)
    end_timestamp = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    timestamp = models.DateTimeField()

    def __str__(self):
        message = self.pivot_id or "Não encontrado"

        return f"Histórico de Agendamentos {message}".upper()
