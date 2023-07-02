from django.contrib import admin
from crud.models import Pivots


@admin.register(Pivots)
class PivotAdmin(admin.ModelAdmin):
    ordering = ["pivot_id"]
    exclude = ("pivot_id", "farm_id")
    list_display = (
        "pivot_id",
        "pivot_lat",
        "pivot_lng",
        "pivot_is_gprs",
        "pivot_ip_gateway",
        "radio_id",
    )
    list_display_links = ["pivot_id"]
    empty_value_display = "Campo descritivo não encontrado"
    list_editable = (
        "pivot_lat",
        "pivot_lng",
        "pivot_is_gprs",
        "pivot_ip_gateway",
        "radio_id",
    )

    actions = ["exclude_pivot"]

    @admin.action(description="Excluir")
    def exclude_pivot(self, request, queryset):
        queryset.delete()
