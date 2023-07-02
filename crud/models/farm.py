from django.db import models
from crud.models import SoilUser
from crud.utils.set_foreign_null import get_sentinel_user

import json


class Farm(models.Model):
    class Meta:
        db_table = "farms"
        verbose_name_plural = "Fazendas"
        verbose_name = "Fazenda"
        ordering = ["id"]
        indexes = [
            models.Index(fields=["farm_name", "farm_id"]),
            models.Index(fields=["farm_name"], name="farm_name_idx"),
        ]

    farm_id = models.CharField(max_length=30, unique=True)
    farm_name = models.CharField(max_length=60)
    farm_city = models.CharField(max_length=60)
    farm_lat = models.FloatField()
    farm_lng = models.FloatField()
    user_id = models.ForeignKey(
        SoilUser, on_delete=models.CASCADE, related_name="owner_of_farm"
    )
    dealer = models.ForeignKey(
        SoilUser,
        on_delete=models.SET(get_sentinel_user),
        related_name="dealers_of_farm",
        blank=True,
        null=True,
    )
    users = models.ManyToManyField(
        SoilUser,
        related_name="users_of_farm",
        blank=True,
    )

    REQUIRED_FIELDS = [
        "farm_id",
        "farm_name",
        "farm_city",
        "farm_lat",
        "farm_lng",
        "user_id",
    ]

    def __str__(self):
        return str(self.farm_name).upper()
