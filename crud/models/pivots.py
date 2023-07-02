from django.db import models
from crud.models import Farm


class Pivots(models.Model):
    class Meta:
        db_table = "pivots"
        verbose_name_plural = "Pivôs"
        verbose_name = "Pivô"
        ordering = ["pivot_num"]
        indexes = [
            models.Index(fields=["pivot_num", "pivot_id"]),
            models.Index(fields=["pivot_num"], name="pivot_num_idx"),
        ]

    pivot_num = models.IntegerField(unique=True)
    pivot_id = models.CharField(max_length=60)
    farm_id = models.ForeignKey(
        Farm, on_delete=models.CASCADE, related_name="farm_of_pivot"
    )
    pivot_lng = models.FloatField()
    pivot_lat = models.FloatField()
    radio_id = models.IntegerField(unique=True)
    pivot_start_angle = models.IntegerField()
    pivot_end_angle = models.IntegerField()
    pivot_is_gprs = models.BooleanField(default=False)
    pivot_ip_gateway = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return str(self.pivot_id).upper()
