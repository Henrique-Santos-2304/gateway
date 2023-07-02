from django.contrib import admin
from crud.models import LastState


@admin.register(LastState)
class LastStateAdmin(admin.ModelAdmin):
    ordering = ("pivot_id", "-id")
    fields = ("angle", "state")
    list_display = ("pivot_id", "angle", "state")
    list_display_links = ["pivot_id"]
    empty_value_display = "Campo descritivo não encontrado"
    list_editable = ("angle", "state")

    actions = ["exclude_last_state"]

    @admin.action(description="Excluir")
    def exclude_last_state(self, request, queryset):
        queryset.delete()
