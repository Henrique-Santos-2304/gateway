from django.db import models
from crud.models import States


class StateVariables(models.Model):
    class Meta:
        db_table = "state_variables"
        verbose_name_plural = "Variáveis dos estados"
        verbose_name = "Variável do estado"
        ordering = ["state_id"]
        indexes = [
            models.Index(fields=["state_id"]),
            models.Index(fields=["state_id"], name="state_id_name_idx"),
        ]

    state_variable_id = models.CharField(max_length=90, blank=True, null=True)
    state_id = models.ForeignKey(
        States, on_delete=models.CASCADE, related_name="state_of_state_variable"
    )
    angle = models.IntegerField()
    percentimeter = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Variaveis de Estado".upper()
