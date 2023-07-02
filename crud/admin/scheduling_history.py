from django.contrib import admin
from crud.models import SchedulingHistory


@admin.register(SchedulingHistory)
class SchedulingHistoryAdmin(admin.ModelAdmin):
    ordering = ("pivot_id", "-id")
    exclude = ("pivot_id", "scheduling_id", "updated", "timestamp")
    list_display = ("pivot_id", "power", "water", "direction", "percentimeter")
    list_display_links = ["pivot_id"]
    empty_value_display = "Campo descritivo não encontrado"
    list_editable = ("power", "water", "direction", "percentimeter")

    actions = ["exclude_scheduling"]

    @admin.action(description="Excluir")
    def exclude_scheduling(self, request, queryset):
        queryset.delete()
