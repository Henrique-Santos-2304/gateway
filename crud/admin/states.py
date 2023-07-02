from django.contrib import admin
from crud.models import States


@admin.register(States)
class StateAdmin(admin.ModelAdmin):
    ordering = ("pivot_id", "-id")
    exclude = ("pivot_id", "state_id", "timestamp")
    list_display = ("pivot_id", "power", "water", "direction", "connection", "pressure")
    list_display_links = ["pivot_id"]
    empty_value_display = "Campo descritivo não encontrado"
    list_editable = ("power", "water", "direction", "connection", "pressure")

    actions = ["exclude_state"]

    @admin.action(description="Excluir")
    def exclude_state(self, request, queryset):
        queryset.delete()
